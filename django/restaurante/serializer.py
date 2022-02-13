from rest_framework import serializers
from restaurante.models import Comida

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = ['id', 'nome', 'valor']