# Generated by Django 4.2.9 on 2024-02-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0032_alter_collaborateur_adresse_postale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Sexe',
            field=models.CharField(blank=True, choices=[('H', 'H'), ('F', 'F')], max_length=5, null=True),
        ),
    ]