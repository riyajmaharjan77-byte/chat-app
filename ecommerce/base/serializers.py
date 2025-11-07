from rest_framework import serializers
from .models import product, producttype

class productserializer(serializers.ModelSerializer):
    class meta:
        model=product
        fields='__all__'
class productviewserializer(serializers.ModelSerializer):
    class meta:
        model=producttype
        fields='__all__'
    