from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from assets import views

from . import views

urlpatterns = [
    path('producttypes/', views.ProductTypeList.as_view()),
    path('producttypes/<int:pk>', views.ProductTypeDetail.as_view()),
    path('moduletypes/', views.ModuleTypeList.as_view()),
    path('moduletypes/<int:pk>', views.ModuleTypeDetail.as_view()),
    path('units/', views.UnitList.as_view()),
    path('units/<int:pk>', views.UnitDetail.as_view()),
    path('modules/', views.ModuleList.as_view()),
    path('modules/<int:pk>', views.ModuleDetail.as_view()),
    path('versions/', views.VersionList.as_view()),
    path('versions/<int:pk>', views.VersionDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
