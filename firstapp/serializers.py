from rest_framework import serializers
class APIKey_serializers(serializers.Serializer):
    name = serializers.CharField(max_length=40)