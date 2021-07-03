from django.contrib import admin

from .models import ProductType, ModuleType, Module, Unit, Version

admin.site.register(ProductType)
admin.site.register(ModuleType)
admin.site.register(Module)
admin.site.register(Unit)
admin.site.register(Version)
