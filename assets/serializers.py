from rest_framework import serializers
from assets.models import ProductType, ModuleType, Unit, Module, Version

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']

    def create(self, validated_data):
        """
        Create and return a new `Product Type` instance, 
        given the validated data.
        """
        return ProductType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ProductType` instance, 
        given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = ['id', 'name']

    def create(self, validated_data):
        """
        Create and return a new `ModuleType` instance, given the validated data.
        """
        return ModuleType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ModuleType` instance, 
        given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'product_type', 'version', 'serial', 'mfg_date']

    def create(self, validated_data):
        """
        Create and return a new `Unit` instance, given the validated data.
        """
        return Unit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Unit` instance, given the validated data.
        """
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.version = validated_data.get('version', instance.version)
        instance.serial = validated_data.get('serial', instance.serial)
        instance.mfg_date = validated_data.get('mfg_date', instance.mfg_date)
        instance.save()
        return instance

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'module_type', 'version', 'serial', 'mfg_date']

    def create(self, validated_data):
        """
        Create and return a new `Module` instance, given the validated data.
        """
        return Module.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Module` instance, 
        given the validated data.
        """
        instance.module_type = validated_data.get('module_type', instance.module_type)
        instance.version = validated_data.get('version', instance.version)
        instance.serial = validated_data.get('serial', instance.serial)
        instance.mfg_date = validated_data.get('mfg_date', instance.mfg_date)
        instance.save()
        return instance

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['id', 'name']

    def create(self, validated_data):
        """
        Create and return a new `Version` instance, given the validated data.
        """
        return Version.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Version` instance, 
        given the validated data.
        """
        instance.name = validated_data.get('name', instance.product_type)
        instance.save()
        return instance
