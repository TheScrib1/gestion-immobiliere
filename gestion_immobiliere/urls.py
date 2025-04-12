from django.contrib import admin
from django.urls import path, include  # <-- ajoute 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_immobiliere_yesoda.urls')),  # <-- ajoute cette ligne
]
