from rest_framework.serializers import ModelSerializer
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
        if instance.status == 'qabul qilindi':
            return {
                'price': instance.price,
                'status': instance.status,
                'preparation_time': "test"
            }
        elif instance.status == 'tayyor':
            return {
                "arrival time": 'test'
            }
        else:
            return representation
