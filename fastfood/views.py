from rest_framework import generics, views, status

from fastfood.api_v1.permission import IsAdminOrWaiter
from rest_framework.permissions import IsAuthenticated
from fastfood.api_v1.serializers import MenuSerializer, OrderItemSerializer, OrderSerializer
from fastfood.models import Food, OrderItem, Order


class FoodApiView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrWaiter, ]


class FoodDetailApView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrWaiter, ]


class CreateOrderItemView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Faqat OrderItemlarni saqlaymiz, Order yaratmaymiz
        serializer.save(user=self.request.user)


from rest_framework.response import Response


class CreateOrderView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Foydalanuvchini avtomatik olamiz
        if not user.is_authenticated:
            return Response({"error": "Foydalanuvchi autentifikatsiyadan o'tmagan"},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Foydalanuvchining barcha OrderItemlarini olamiz
        order_items = OrderItem.objects.filter(user=user, order__isnull=True)
        if not order_items.exists():
            return Response({"error": "Hech qanday order item topilmadi"}, status=status.HTTP_400_BAD_REQUEST)
        new_order = Order.objects.create(user=user, price=0, status='jarayonda')

        total_price = 0
        for item in order_items:
            item.order = new_order
            item.save()
            total_price += item.food.price * item.quantity

        new_order.price = total_price
        new_order.save()

        serializer = OrderSerializer(new_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user  # Foydalanuvchini avtomatik olamiz
        if not user.is_authenticated:
            return Response({"error": "Foydalanuvchi autentifikatsiyadan o'tmagan"},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Foydalanuvchiga tegishli barcha Orderlarni olamiz
        user_orders = Order.objects.filter(user=user)
        if not user_orders.exists():
            return Response({"message": "Sizda hali buyurtmalar mavjud emas"}, status=status.HTTP_200_OK)

        # Orderlarni serializer orqali formatlaymiz
        serializer = OrderSerializer(user_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
