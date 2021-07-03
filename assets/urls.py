from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('units/<int:unit_id>', views.units, name='units'),
    path('modules/<int:module_id>', views.modules, name='modules'),
]
