from django.shortcuts import render
from rest_framework import generics

from fastfood.api_v1.permission import IsAdminOrWaiter
from rest_framework.permissions import IsAuthenticated
from fastfood.api_v1.serializers import MenuSerializer, OrderItemSerializer
from fastfood.models import Food, OrderItem


class FoodApiView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrWaiter,]


class FoodDetailApView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrWaiter,]


class OrderItemListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Faqat foydalanuvchiga tegishli buyurtmalarni qaytarish
        return OrderItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Yangi buyurtma yaratilayotganda user ni avtomatik belgilash
        serializer.save(user=self.request.user)