from rest_framework import viewsets
from rest_framework.response import Response
from django.http import  JsonResponse

from .models import ( ModelB, ModelC,ModelB1,ModelB2,
        ModelC1, ModelC2 ,ModelD, Product, ModelA )
from .serializers import ( ModelB1Serializer, ModelC1Serializer,
    ModelB2Serializer, ModelC2Serializer , ModelDSerializer,
    ModelASerializer, ModelBSerializer, ModelCSerializer)

class ModelB1ViewSet(viewsets.ModelViewSet):
    serializer_class = ModelB1Serializer
    queryset = ModelB1.objects.all()

class ModelB2ViewSet(viewsets.ModelViewSet):
    serializer_class = ModelB2Serializer
    queryset = ModelB2.objects.all()

class ModelC1ViewSet(viewsets.ModelViewSet):
    serializer_class = ModelC1Serializer
    queryset = ModelC1.objects.all()

class ModelC2ViewSet(viewsets.ModelViewSet):
    serializer_class = ModelC2Serializer
    queryset = ModelC2.objects.all()

class ModelDViewSet(viewsets.ModelViewSet):
    serializer_class = ModelDSerializer
    queryset = ModelD.objects.all()

class ModelAViewSet(viewsets.ModelViewSet):
    serializer_class = ModelASerializer
    queryset = ModelA.objects.all()

class ModelBViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ModelBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = dict ( variableB1 = ModelB1.objects.get(pk=serializer.data.get("variableB1")).name,
                variableB2 = serializer.data.get("variableB2"),
                variableB3 = ModelB2.objects.get(pk=serializer.data.get("variableB3")).name,
                variableB4 = ModelB1.objects.get(pk=serializer.data.get("variableB4")).name,
                variableB5 = serializer.data.get("variableB5"),
                )
            return JsonResponse(data, safe= False)

class ModelCViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = ModelCSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            data = dict ( variableC1 = ModelC1.objects.get(pk=serializer.data.get("variableC1")).name,
                variableC2 = serializer.data.get("variableC2"),
                variableC3 = ModelC2.objects.get(pk=serializer.data.get("variableC3")).name,
                variableC4 = ModelC1.objects.get(pk=serializer.data.get("variableC4")).name,
                variableC5 = serializer.data.get("variableC5"),
                )
            return JsonResponse(data, safe= False)

#
# class ModelBViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = ModelB.objects.all()
#         serializer = ModelBSerializer (queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ModelBSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
#
# class ModelCViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = ModelC.objects.all()
#         serializer = ModelCSerializer (queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ModelCSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
