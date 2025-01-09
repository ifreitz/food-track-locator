import os

from django.core.management import call_command
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
