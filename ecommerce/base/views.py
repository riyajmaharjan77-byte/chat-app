from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import product, producttype
from .serializers import productserializer, productviewserializer
from rest_framework.response import Response
# Create your views here.
class productviewset(ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productserializer

class producttypeview(GenericViewSet):
    queryset=producttype.objects.all()
    serializer_class=productviewserializer

    def list(self,request):
        queryset=self.get_queryset()
        serializer= self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def retrieve(self, request, pk=None):
        instance = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        instance = self.get_queryset().get(pk=pk)
        instance.delete()
        return Response({"message": "Deleted successfully"})
    
