import os

from django.core.management import call_command
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from geopy.distance import geodesic

from api.models import FoodTruck
from api.serializers import FoodTruckSerializer


class ImportFoodTrucksView(APIView):
    @swagger_auto_schema(
        operation_description="Import food truck data from CSV file",
        responses={
            200: openapi.Response(
                description="Data imported successfully",
                examples={
                    "application/json": {
                        "message": "Food truck data imported successfully"
                    }
                }
            ),
            404: openapi.Response(
                description="CSV file not found",
                examples={
                    "application/json": {
                        "error": "CSV file not found"
                    }
                }
            ),
            500: openapi.Response(
                description="Internal server error",
                examples={
                    "application/json": {
                        "error": "Error message details"
                    }
                }
            )
        }
    )
    def post(self, request):
        try:
            csv_file = 'food-truck-data.csv'
            if not os.path.exists(csv_file):
                return Response(
                    {'error': 'CSV file not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            call_command('import_food_trucks', csv_file)
            return Response(
                {'message': 'Food truck data imported successfully'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FoodTruckListView(APIView):
    @swagger_auto_schema(
        operation_description="Get all food trucks",
        responses={
            200: openapi.Response(
                description="Food trucks retrieved successfully",
                examples={
                    "application/json": {
                        "food_trucks": [{"id": 1, "name": "Food Truck 1"}, {"id": 2, "name": "Food Truck 2"}]
                    }
                }
            )
        }
    )
    def get(self, request):
        food_trucks = FoodTruck.objects.all()
        serializer = FoodTruckSerializer(food_trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodTruckFilterView(APIView):
    @swagger_auto_schema(
        operation_description="Get food trucks within a certain distance from a given latitude and longitude",
        manual_parameters=[
            openapi.Parameter('lat', openapi.IN_QUERY, description="Latitude of the location. Example: 37.7749", type=openapi.TYPE_NUMBER, required=True, example=37.7749),
            openapi.Parameter('lon', openapi.IN_QUERY, description="Longitude of the location. Example: -122.4194", type=openapi.TYPE_NUMBER, required=True, example=-122.4194),
            openapi.Parameter('limit', openapi.IN_QUERY, description="Number of food trucks to return", type=openapi.TYPE_INTEGER, required=False, example=5, default=5)
        ],
        responses={
            200: openapi.Response(
                description="Food trucks retrieved successfully",
                examples={
                    "application/json": {
                        "food_trucks": [
                            {"id": 1, "name": "Food Truck 1"},
                            {"id": 2, "name": "Food Truck 2"}
                        ]
                    }
                }
            )
        }
    )

    def get(self, request):
        """
        Get the nearest food trucks from a given latitude and longitude

        Parameters:
        lat: float
            The latitude of the location
        lon: float
            The longitude of the location
        limit: int
            The number of food trucks to return
        """
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        limit = request.query_params.get('limit', 5)

        if not lat or not lon:
            return Response(
                {'error': 'Latitude and longitude are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        food_trucks = self.get_nearest_food_trucks(lat, lon, limit)
        serializer = FoodTruckSerializer(food_trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_nearest_food_trucks(self, lat, lon, limit=5):
        """
        Get the nearest food trucks from a given latitude and longitude
        """
        lat = float(lat)
        lon = float(lon)
        limit = int(limit)

        cache_key = f'nearest_food_trucks_{lat}_{lon}_{limit}'
        cached_food_trucks = cache.get(cache_key)

        if cached_food_trucks is not None:
            return cached_food_trucks

        food_trucks = FoodTruck.objects.all()
        food_trucks_with_distance = []

        for truck in food_trucks:
            distance = geodesic((lat, lon), (truck.latitude, truck.longitude)).km
            food_trucks_with_distance.append((truck, distance))

        # Sort by distance
        food_trucks_with_distance.sort(key=lambda x: x[1])

        # Return nearest food trucks
        nearest_trucks = [truck[0] for truck in food_trucks_with_distance[:limit]]

        # Cache the result
        cache.set(cache_key, nearest_trucks)

        return nearest_trucks
