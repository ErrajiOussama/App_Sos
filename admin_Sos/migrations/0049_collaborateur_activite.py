# Generated by Django 4.2.9 on 2024-02-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0048_salaire_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateur',
            name='Activite',
            field=models.CharField(blank=True, choices=[('FRANCE', 'FRANCE'), ('CANADA', 'CANADA')], max_length=10, null=True),
        ),
    ]
