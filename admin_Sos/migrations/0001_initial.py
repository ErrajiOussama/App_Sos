# Generated by Django 4.2.9 on 2024-02-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statut', models.CharField(max_length=10)),
                ('Nom', models.CharField(max_length=10)),
                ('Prenom', models.CharField(max_length=10)),
                ('Sexe', models.CharField(max_length=5)),
                ('Date_de_naissance', models.DateField()),
                ('Age', models.IntegerField()),
                ('Situation_familiale', models.CharField(max_length=10)),
                ('Nombre_d_enfants', models.FloatField()),
                ('N_CIN', models.CharField(max_length=12)),
                ('N_Passeport', models.CharField(max_length=30)),
                ('Nationalité', models.CharField(max_length=20)),
                ('Adresse_postale', models.CharField(max_length=50)),
                ('Ville', models.CharField(max_length=20)),
                ('E_mail', models.EmailField(max_length=254)),
                ('N_de_téléphone', models.CharField(max_length=20)),
                ('RIB', models.CharField(max_length=30)),
                ('N_CNSS', models.CharField(max_length=20)),
                ('Type_de_contrat', models.CharField(max_length=10)),
                ('Rémunération', models.IntegerField()),
                ('Prime', models.FloatField()),
                ('Poste', models.CharField(max_length=10)),
                ('Date_d_entrée', models.DateField()),
                ('Date_de_Sortie', models.DateField()),
            ],
        ),
    ]
