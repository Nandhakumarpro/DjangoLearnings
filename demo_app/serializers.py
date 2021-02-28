from rest_framework import serializers
from .models import ( ModelB, ModelC,ModelB1,ModelB2,
        ModelC1, ModelC2 ,ModelD, Product,ModelA )

class ModelB1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB1
        fields = ("name", )

class ModelB2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB2
        fields = ("name", )

class ModelC1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModelC1
        fields = ("name", )

class ModelC2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModelC2
        fields = ("name", )

class ModelDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelD
        fields = ("name", )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ModelBSerializer(serializers.ModelSerializer):
    ''''''
    # variableB1 = serializers.ChoiceField( choices = ModelB1.objects.all() , required= True)
    # variableB2 = serializers.IntegerField(required =True )
    # variableB3 = serializers.ChoiceField( choices = ModelB2.objects.all() , required= True)
    # variableB4 = serializers.ChoiceField( choices = ModelB1.objects.all() , required= True)
    # variableB5 = serializers.IntegerField(required =True )
    # product = serializers.ChoiceField( choices = ModelB1.objects.all() , required= True)
    class Meta:
        model = ModelB
        fields = "__all__"

class ModelCSerializer(serializers.ModelSerializer):
    ''''''
    # variableC1 = serializers.ChoiceField( choices = ModelC1.objects.all() , required= True)
    # variableC2 = serializers.IntegerField(required =True )
    # variableC3 = serializers.ChoiceField( choices = ModelC2.objects.all() , required= True)
    # variableC4 = serializers.ChoiceField( choices = ModelC1.objects.all() , required= True)
    # variableC5 = serializers.IntegerField(required =True )
    class Meta:
        model = ModelC
        fields = "__all__"

class ModelASerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelA
        fields = "__all__"
