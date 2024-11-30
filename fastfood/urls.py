from django.urls import path

from fastfood.views import FoodApiView, FoodDetailApView, CreateOrderView, CreateOrderItemView, OrderListAPIView

app_name = 'api'

urlpatterns = [
    path('foods/', FoodApiView.as_view(), name='foods'),
    path('food/<int:pk>', FoodDetailApView.as_view(), name='food-detail'),
    path('order-create/', CreateOrderView.as_view(), name='order-create'),
    path('order/', OrderListAPIView.as_view(), name='order'),
    path('order-item-create/', CreateOrderItemView.as_view(), name='order_item-create'),
]
