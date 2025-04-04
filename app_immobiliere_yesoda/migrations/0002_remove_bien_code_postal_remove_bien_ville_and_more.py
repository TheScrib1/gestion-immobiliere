# Generated by Django 5.2 on 2025-04-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_immobiliere_yesoda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bien',
            name='code_postal',
        ),
        migrations.RemoveField(
            model_name='bien',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='locataire',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='proprietaire',
            name='prenom',
        ),
        migrations.AddField(
            model_name='bien',
            name='compteur_eau',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bien',
            name='compteur_electricite',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bien',
            name='compteur_gaz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bien',
            name='contrat_pdf',
            field=models.FileField(blank=True, null=True, upload_to='contrats/'),
        ),
        migrations.AddField(
            model_name='bien',
            name='etat_lieux_entree',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bien',
            name='etat_lieux_sortie',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bien',
            name='loyer',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bien',
            name='surface',
            field=models.FloatField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locataire',
            name='date_sortie',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locataire',
            name='remarques',
            field=models.TextField(blank=True),
        ),
    ]
