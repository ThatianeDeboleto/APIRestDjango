from django.contrib import admin
from django.urls import path, include
from restaurante.views import ComidasViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'comidas', ComidasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
