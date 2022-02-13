from django.contrib import admin
from restaurante.models import Comida

class Comidas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Comida, Comidas)