from django.db import models

# ========================
# Propriétaire
# ========================
class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    numero_whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}" if self.prenom else self.nom


# ========================
# Locataire
# ========================
class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    numero_whatsapp = models.CharField(max_length=20, blank=True, null=True)
    num_cni_passport = models.CharField(max_length=50, blank=True, null=True)
    documents_pdf = models.FileField(upload_to='documents_locataires/', blank=True, null=True)
    notes_service = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# ========================
# Bien immobilier
# ========================
DEVISE_CHOICES = [
    ('XOF', 'Franc CFA (FCFA)'),
    ('EUR', 'Euro (€)'),
    ('USD', 'Dollar ($)'),
    ('GBP', 'Livre (£)'),
    ('AUTRE', 'Autre'),
]

class Bien(models.Model):
    nom = models.CharField(max_length=255, default="Nom du bien", verbose_name="Nom du bien")
    type_bien = models.CharField(max_length=255, default="description", verbose_name="Description du bien", help_text="Duplex, immeuble, magasin, entrepôt…")
    quartier = models.CharField(max_length=255, blank=True, verbose_name="Quartier")
    ville = models.CharField(max_length=255, verbose_name="Ville")
    adresse = models.CharField(max_length=255, verbose_name="Adresse complète")
    surface = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Surface en m²")
    loyer = models.PositiveIntegerField(verbose_name="Loyer", help_text="Montant en chiffres (ex : 100000)")
    devise = models.CharField(max_length=10, choices=DEVISE_CHOICES, default='XOF', verbose_name="Devise")
    locataire = models.ForeignKey('Locataire', on_delete=models.SET_NULL, null=True, blank=True, help_text="Locataire actuellement lié à ce bien (facultatif).")
    proprietaire = models.ForeignKey('Proprietaire', on_delete=models.CASCADE, help_text="Propriétaire du bien (obligatoire).")

    def __str__(self):
        return f"{self.nom} - {self.ville}"


# ========================
# Technicien
# ========================
class Technicien(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    numero_whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.specialite}"


# ========================
# Intervention
# ========================
class Intervention(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Technicien, on_delete=models.SET_NULL, null=True, blank=True)
    date_intervention = models.DateField()
    description = models.TextField()
    rdv_fixe_avec_locataire = models.DateTimeField(blank=True, null=True)
    marge_prevue = models.DurationField(default=0)
    retour_client_commentaire = models.TextField(blank=True, null=True)
    retour_client_note = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Intervention sur {self.bien} le {self.date_intervention}"


# ========================
# Mission du jour (Gestionnaire)
# ========================
class MissionDuJour(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En Cours'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée'),
    ]

    date = models.DateField()
    budget_estime = models.DecimalField(max_digits=10, decimal_places=2)
    taches = models.TextField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_cours')

    def __str__(self):
        return f"Mission du {self.date} - Statut: {self.get_statut_display()}"
