from rest_framework import viewsets
from rest_framework.response import Response

from .models import ModelB, ModelC
from .serializers import ModelBSerializer, ModelCSerializer

class ModelBViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ModelB.objects.all()
        serializer = ModelBSerializer (queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ModelBSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

class ModelCViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ModelC.objects.all()
        serializer = ModelCSerializer (queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ModelCSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
