from django.db import models

# Create your models here.

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
