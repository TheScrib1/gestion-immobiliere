from django.db import models

class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_entree = models.DateField()
    date_sortie = models.DateField(null=True, blank=True)
    remarques = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Bien(models.Model):
    adresse = models.CharField(max_length=255)
    surface = models.FloatField()
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.SET_NULL, null=True, blank=True)

    contrat_pdf = models.FileField(upload_to='contrats/', null=True, blank=True)
    compteur_eau = models.IntegerField(default=0)
    compteur_electricite = models.IntegerField(default=0)
    compteur_gaz = models.IntegerField(default=0)
    etat_lieux_entree = models.TextField(blank=True)
    etat_lieux_sortie = models.TextField(blank=True)

    def __str__(self):
        return self.adresse


class Technicien(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.specialite}"


class Intervention(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Technicien, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    duree_estimee = models.DurationField(help_text="Durée estimée (hh:mm:ss)")
    marge_prevue = models.DurationField(default="01:30:00", help_text="Marge pour imprévus (hh:mm:ss)")
    evaluation = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Note donnée par le locataire (1-5)")

    def __str__(self):
        return f"Intervention sur {self.bien.adresse} par {self.technicien.nom} le {self.date.strftime('%d/%m/%Y')}"

