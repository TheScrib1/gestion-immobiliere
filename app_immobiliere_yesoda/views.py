from django.shortcuts import render, get_object_or_404, redirect
from .models import Technicien, Proprietaire, Bien  # Ajoute Bien ici
from .forms import TechnicienForm, ProprietaireForm

# 🔹 Vue de la page d'accueil
def accueil(request):
    biens = Bien.objects.select_related('locataire', 'proprietaire')
    return render(request, 'accueil.html', {'biens': biens})

# 🔹 Liste des techniciens (filtrable par spécialité)
def liste_techniciens(request):
    specialite = request.GET.get('specialite')
    if specialite:
        techniciens = Technicien.objects.filter(specialite__icontains=specialite)
    else:
        techniciens = Technicien.objects.all()
    return render(request, 'techniciens/liste.html', {'techniciens': techniciens})

# 🔹 Détail d’un technicien
def detail_technicien(request, technicien_id):
    technicien = get_object_or_404(Technicien, id=technicien_id)
    return render(request, 'techniciens/detail.html', {'technicien': technicien})

# 🔹 Ajout d’un technicien
def ajouter_technicien(request):
    if request.method == 'POST':
        form = TechnicienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_techniciens')
    else:
        form = TechnicienForm()
    return render(request, 'techniciens/ajouter.html', {'form': form})

# 🔹 Ajout d’un propriétaire
def ajouter_proprietaire(request):
    if request.method == 'POST':
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')  # Ou autre page après ajout
    else:
        form = ProprietaireForm()
    return render(request, 'proprietaires/ajouter.html', {'form': form})
