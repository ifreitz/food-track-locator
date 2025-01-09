from django.urls import path
from api.views import ImportFoodTrucksView, FoodTruckListView, FoodTruckFilterView

urlpatterns = [
    path('food-trucks/', FoodTruckListView.as_view(), name='food-truck-list'),
    path('import-food-trucks/', ImportFoodTrucksView.as_view(), name='import-food-trucks'),
    path('nearest-food-trucks/', FoodTruckFilterView.as_view(), name='nearest-food-trucks'),
] 