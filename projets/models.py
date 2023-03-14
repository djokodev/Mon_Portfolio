from django.db import models

class Projet(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.nom
