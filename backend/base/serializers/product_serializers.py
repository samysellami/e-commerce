from rest_framework import fields, serializers
from django.contrib.auth.models import User
from base.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
