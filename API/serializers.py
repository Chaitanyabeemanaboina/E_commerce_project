from rest_framework.serializers import ModelSerializer
from firstapp.models import Products
class Product_serializers(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
