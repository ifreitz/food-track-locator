from django.urls import path
from .views import ImportFoodTrucksView

urlpatterns = [
    path('import-food-trucks/', ImportFoodTrucksView.as_view(), name='import-food-trucks'),
] 