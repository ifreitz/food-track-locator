from django.urls import path
from api.views import ImportFoodTrucksView, FoodTruckListView

urlpatterns = [
    path('food-trucks/', FoodTruckListView.as_view(), name='food-truck-list'),
    path('import-food-trucks/', ImportFoodTrucksView.as_view(), name='import-food-trucks'),
] 