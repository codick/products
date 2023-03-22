from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    size = serializers.IntegerField(default=13)
    manufacturer_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.size = validated_data.get("size", instance.size)
        instance.manufacturer_id = validated_data.get("manufacturer_id", instance.manufacturer_id)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.price = validated_data.get("price", instance.price)
        instance.save()

        return instance
