from rest_framework import serializers
from .models import ModelB, ModelC

class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = "__all__"

class ModelCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelC
        fields = "__all__"
