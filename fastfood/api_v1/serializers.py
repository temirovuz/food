from rest_framework.serializers import ModelSerializer

from fastfood.function import distance, get_user_order_items_quantity, to_divide_into_a_unit_of_time
from fastfood.models import User, Food, OrderItem, Order


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'role']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food', 'quantity']
        read_only_fields = ['user']  # User avtomatik belgilanadi


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'price', 'status', 'items']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = instance.user
        user_lat = getattr(user, 'latitude', None)
        user_lon = getattr(user, 'longitude', None)

        if instance.status == 'qabul qilindi':
            preparation_time = get_user_order_items_quantity(user)
            return {
                'price': instance.price,
                'status': instance.status,
                'quantity': f"{preparation_time} ta buyurtma",
                'preparation_time': to_divide_into_a_unit_of_time(preparation_time * 2)
            }
        elif instance.status == 'tayyor':
            distance_to_client = distance(user_lat, user_lon)
            arrival_time = float(f"{distance_to_client:.2f}")
            return {
                "distance": f"{distance_to_client:.2f} km",
                "arrival time": to_divide_into_a_unit_of_time(arrival_time * 3)
            }
        else:
            return representation
