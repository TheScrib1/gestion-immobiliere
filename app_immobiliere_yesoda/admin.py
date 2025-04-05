from django.contrib import admin
from .models import Proprietaire, Locataire, Bien, Technicien, Intervention

@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'email')

@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'email', 'date_entree', 'date_sortie')

@admin.register(Bien)
class BienAdmin(admin.ModelAdmin):
    list_display = ('adresse', 'surface', 'loyer', 'proprietaire', 'locataire')

@admin.register(Technicien)
class TechnicienAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'specialite')

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('bien', 'technicien', 'date', 'duree_estimee', 'evaluation')
    list_filter = ('technicien', 'date')
    search_fields = ('bien__adresse', 'technicien__nom', 'description')
