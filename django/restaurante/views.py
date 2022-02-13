from django.shortcuts import render
from rest_framework import viewsets
from restaurante.models import Comida
from restaurante.serializer import ComidaSerializer


class ComidasViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

