# biler/models.py
from django.db import models

class Bil(models.Model):
    registreringsnummer = models.CharField(max_length=10, unique=True)
    merke = models.CharField(max_length=50)
    modell = models.CharField(max_length=50)
    arsmodell = models.IntegerField()
    kilometerstand = models.IntegerField()

    # Status
    til_salgs = models.BooleanField(default=False)
    pris = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Oversikt
    aktiv = models.BooleanField(default=True)  # finnes fortsatt i bilparken

    def __str__(self):
        return f"{self.merke} {self.modell} ({self.registreringsnummer})"