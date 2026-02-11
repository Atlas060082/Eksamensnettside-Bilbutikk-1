from django.db import models
from django.utils import timezone

class Bil(models.Model):
    merke = models.CharField(max_length=100)
    modell = models.CharField(max_length=100)
    årsmodell = models.IntegerField()
    regnummer = models.CharField(max_length=10, unique=True)
    kilometerstand = models.IntegerField()
    
    drivstoff = models.CharField(max_length=50)
    girkasse = models.CharField(max_length=50)
    farge = models.CharField(max_length=50)
    
    innkjøpspris = models.DecimalField(max_digits=10, decimal_places=2)
    salgspris = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(
        max_length=50,
        choices=[
            ('innkommet', 'Innkommet'),
            ('under_service', 'Under service'),
            ('klar_salg', 'Klar for salg'),
            ('solgt', 'Solgt'),
        ],
        default='innkommet'
    )
    
    beskrivelse = models.TextField(blank=True)
    bilde = models.ImageField(upload_to='bil_bilder/', blank=True, null=True)
    
    innkommet_dato = models.DateField(default=timezone.now)
    opprettet = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Biler"
        ordering = ['-innkommet_dato']
    
    def __str__(self):
        return f"{self.merke} {self.modell} ({self.årsmodell})"


class Service(models.Model):
    bil = models.ForeignKey(Bil, on_delete=models.CASCADE, related_name='servicer')
    
    type = models.CharField(max_length=100)
    beskrivelse = models.TextField()
    planlagt_dato = models.DateField()
    
    estimert_kostnad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    faktisk_kostnad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    fullført = models.BooleanField(default=False)
    fullført_dato = models.DateField(blank=True, null=True)
    
    ansvarlig = models.CharField(max_length=100, blank=True)
    notater = models.TextField(blank=True)
    
    opprettet = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Servicer"
        ordering = ['-planlagt_dato']
    
    def __str__(self):
        return f"{self.type} - {self.bil.regnummer}"