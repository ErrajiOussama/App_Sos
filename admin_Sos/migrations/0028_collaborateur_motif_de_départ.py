# Generated by Django 4.2.9 on 2024-02-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0027_collaborateur_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateur',
            name='Motif_de_départ',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
