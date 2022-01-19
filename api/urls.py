
from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register('BusStatusData',views.BusSatusDataViewSet,basename='BusStatusData')

urlpatterns = [
    path('',include(routers.urls)),
]
