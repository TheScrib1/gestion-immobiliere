# Generated by Django 5.2 on 2025-04-11 12:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_immobiliere_yesoda', '0006_missiondujour_bien_missions_du_jour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bien',
            options={},
        ),
        migrations.AlterModelOptions(
            name='intervention',
            options={},
        ),
        migrations.AlterModelOptions(
            name='locataire',
            options={},
        ),
        migrations.AlterModelOptions(
            name='missiondujour',
            options={},
        ),
        migrations.AlterModelOptions(
            name='proprietaire',
            options={},
        ),
        migrations.AlterModelOptions(
            name='technicien',
            options={},
        ),
        migrations.RemoveField(
            model_name='bien',
            name='compteur_eau',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='compteur_electricite',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='compteur_gaz',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='contrat_pdf',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='est_loue',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='etage_porte',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='etat_lieux_entree',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='etat_lieux_sortie',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='missions_du_jour',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='date',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='duree_estimee',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='locataire',
            name='date_entree',
        ),
        migrations.RemoveField(
            model_name='locataire',
            name='date_sortie',
        ),
        migrations.RemoveField(
            model_name='locataire',
            name='remarques',
        ),
        migrations.RemoveField(
            model_name='missiondujour',
            name='budget_alloue',
        ),
        migrations.RemoveField(
            model_name='missiondujour',
            name='description',
        ),
        migrations.RemoveField(
            model_name='missiondujour',
            name='remarque',
        ),
        migrations.RemoveField(
            model_name='missiondujour',
            name='statut',
        ),
        migrations.AddField(
            model_name='bien',
            name='devise',
            field=models.CharField(choices=[('XOF', 'Franc CFA (FCFA)'), ('EUR', 'Euro (€)'), ('USD', 'Dollar ($)'), ('GBP', 'Livre (£)'), ('AUTRE', 'Autre')], default='XOF', max_length=10, verbose_name='Devise'),
        ),
        migrations.AddField(
            model_name='bien',
            name='nom',
            field=models.CharField(default='Nom du bien', max_length=255, verbose_name='Nom du bien'),
        ),
        migrations.AddField(
            model_name='bien',
            name='quartier',
            field=models.CharField(blank=True, max_length=255, verbose_name='Quartier'),
        ),
        migrations.AddField(
            model_name='bien',
            name='type_bien',
            field=models.CharField(default='description', help_text='Duplex, immeuble, magasin, entrepôt…', max_length=255, verbose_name='Description du bien'),
        ),
        migrations.AddField(
            model_name='bien',
            name='ville',
            field=models.CharField(default='Adresse temporaire', max_length=255, verbose_name='Ville'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervention',
            name='date_intervention',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervention',
            name='rdv_fixe_avec_locataire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='retour_client_commentaire',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='retour_client_note',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locataire',
            name='documents_pdf',
            field=models.FileField(blank=True, null=True, upload_to='documents_locataires/'),
        ),
        migrations.AddField(
            model_name='locataire',
            name='notes_service',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locataire',
            name='num_cni_passport',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='locataire',
            name='numero_whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='locataire',
            name='prenom',
            field=models.CharField(default='Prénom', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='missiondujour',
            name='budget_estime',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='missiondujour',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='missiondujour',
            name='taches',
            field=models.TextField(default='Aucune tâche définie', help_text='Liste des tâches prévues'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='numero_whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='prenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='technicien',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='technicien',
            name='numero_whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='adresse',
            field=models.CharField(max_length=255, verbose_name='Adresse complète'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='locataire',
            field=models.ForeignKey(blank=True, help_text='Locataire actuellement lié à ce bien (facultatif).', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_immobiliere_yesoda.locataire'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='loyer',
            field=models.PositiveIntegerField(help_text='Montant en chiffres (ex : 100000)', verbose_name='Loyer'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='proprietaire',
            field=models.ForeignKey(help_text='Propriétaire du bien (obligatoire).', on_delete=django.db.models.deletion.CASCADE, to='app_immobiliere_yesoda.proprietaire'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='surface',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Surface en m²'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='bien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_immobiliere_yesoda.bien'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='marge_prevue',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='technicien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_immobiliere_yesoda.technicien'),
        ),
        migrations.AlterField(
            model_name='locataire',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='locataire',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='locataire',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='missiondujour',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='technicien',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='technicien',
            name='specialite',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='technicien',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
