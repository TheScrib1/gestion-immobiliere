from django.urls import path
from .views import (
    accueil,
    liste_techniciens,
    detail_technicien,
    ajouter_technicien,
    ajouter_proprietaire,
)

urlpatterns = [
    path('', accueil, name='accueil'),
    path('techniciens/', liste_techniciens, name='liste_techniciens'),
    path('techniciens/<int:technicien_id>/', detail_technicien, name='detail_technicien'),
    path('techniciens/ajouter/', ajouter_technicien, name='ajouter_technicien'),
    path('proprietaires/ajouter/', ajouter_proprietaire, name='ajouter_proprietaire'),
]
