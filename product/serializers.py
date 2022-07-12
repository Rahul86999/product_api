from rest_framework import serializers
from .models import ProductCateogry,Product


class ProductCateogrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCateogry
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class SearchSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','product_name', 'product_image','price','color', 
        'category']

    def get_category(self, obj):
        return obj.product_category.name_category
    