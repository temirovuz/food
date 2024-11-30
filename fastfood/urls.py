from django.urls import path

from fastfood.views import FoodApiView, FoodDetailApView, OrderItemListCreateView

app_name = 'api'

urlpatterns = [
    path('foods/', FoodApiView.as_view(), name='foods'),
    path('orders/', OrderItemListCreateView.as_view(), name='orders'),
    path('food/<int:pk>', FoodDetailApView.as_view(), name='food-detail'),
]
