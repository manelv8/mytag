from django.db import models

# Create your models here.

class Perfil(models.Model):
	url = models.URLField(blank=True)

