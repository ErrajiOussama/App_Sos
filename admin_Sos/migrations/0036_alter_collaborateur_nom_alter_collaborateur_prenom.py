# Generated by Django 4.2.9 on 2024-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0035_alter_collaborateur_salaire_avancee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
