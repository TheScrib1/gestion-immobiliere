from django.contrib import admin
from django.urls import path, include  # <- important pour inclure les urls d'app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_immobiliere_yesoda.urls')),  # <- ici on inclut ton app
]
