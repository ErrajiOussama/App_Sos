# Generated by Django 4.2.9 on 2024-02-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0014_collaborateur_log_alter_collaborateur_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Adresse_postale',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_CNSS',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_de_téléphone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Nationalité',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Poste',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='RIB',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Type_de_contrat',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Ville',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
