from rest_framework.serializers import ModelSerializer
from fastfood.models import User, Food, OrderItem


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'role']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class OrderItemSerializer(ModelSerializer):
    # food = MenuSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'user', 'food', 'quantity']
        read_only_fields = ['user']  # User avtomatik belgilanadi