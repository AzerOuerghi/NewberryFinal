from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            "id", 
            "name",
            "get_absolute_url",
            "description",
            "link",
            "get_image",
            "date_added",
            "category"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )