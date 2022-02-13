from django.db import models

class Comida(models.Model):
      nome = models.CharField(max_length=30)
      valor = models.CharField(max_length=9)

      def __str__(self):
          return self.nome


