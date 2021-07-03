from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductType, ModuleType, Unit, Module, Version
from .serializers import ProductTypeSerializer, ModuleTypeSerializer, UnitSerializer, ModuleSerializer, VersionSerializer

class ProductTypeList(generics.ListCreateAPIView):
    """
    List all units, or create a new Product Type.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Product Type.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
class ModuleTypeList(generics.ListCreateAPIView):
    """
    List all units, or create a new Module.
    """
    queryset = ModuleType.objects.all()
    serializer_class = ModuleTypeSerializer

class ModuleTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Module Type.
    """
    queryset = ModuleType.objects.all()
    serializer_class = ModuleTypeSerializer

class UnitList(generics.ListCreateAPIView):
    """
    List all units, or create a new unit.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a unit instance.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ModuleList(generics.ListCreateAPIView):
    """
    List all modules, or create a new module.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a module instance.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    
class VersionList(generics.ListCreateAPIView):
    """
    List all units, or create a new version.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

class VersionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a version.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
