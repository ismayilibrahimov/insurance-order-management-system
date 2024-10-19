from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'status', 'created_at', 'due_date']
        read_only_fields = ['status', 'created_at', 'due_date']
