# Generated by Django 4.2.9 on 2024-02-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0031_alter_collaborateur_motif_de_départ_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Adresse_postale',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]