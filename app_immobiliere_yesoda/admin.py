from django.contrib import admin
from .models import (
    Proprietaire,
    Locataire,
    Bien,
    Technicien,
    Intervention,
    MissionDuJour,
)


@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "telephone", "email", "numero_whatsapp")
    search_fields = ("nom", "prenom", "telephone", "email")


@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "telephone", "email", "numero_whatsapp", "num_cni_passport")
    search_fields = ("nom", "prenom", "telephone", "email", "num_cni_passport")


@admin.register(Bien)
class BienAdmin(admin.ModelAdmin):
    list_display = ("nom", "type_bien", "ville", "quartier", "surface", "loyer", "devise", "locataire", "proprietaire")
    list_filter = ("ville", "type_bien", "devise")
    search_fields = ("nom", "ville", "quartier", "adresse")
    autocomplete_fields = ("locataire", "proprietaire")


@admin.register(Technicien)
class TechnicienAdmin(admin.ModelAdmin):
    list_display = ("nom", "specialite", "telephone", "email", "numero_whatsapp")
    search_fields = ("nom", "specialite", "telephone")


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("bien", "technicien", "date_intervention", "rdv_fixe_avec_locataire", "retour_client_note")
    list_filter = ("date_intervention",)
    search_fields = ("bien__nom", "technicien__nom")
    autocomplete_fields = ("bien", "technicien")


@admin.register(MissionDuJour)
class MissionDuJourAdmin(admin.ModelAdmin):
    list_display = ("date", "budget_estime", "statut")
    list_filter = ("statut", "date")
    search_fields = ("taches",)
