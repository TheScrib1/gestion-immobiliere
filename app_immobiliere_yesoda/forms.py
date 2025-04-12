from django import forms
from .models import (
    Proprietaire,
    Locataire,
    Bien,
    Technicien,
    Intervention,
    MissionDuJour,
)

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = '__all__'

class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire
        fields = '__all__'

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = '__all__'

class TechnicienForm(forms.ModelForm):
    class Meta:
        model = Technicien
        fields = '__all__'

class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = '__all__'
        widgets = {
            'rdv_fixe_avec_locataire': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_intervention': forms.DateInput(attrs={'type': 'date'}),
        }

class MissionDuJourForm(forms.ModelForm):
    class Meta:
        model = MissionDuJour
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
