# Generated by Django 4.2.9 on 2024-02-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0033_alter_collaborateur_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Poste',
            field=models.CharField(blank=True, choices=[('Agent', 'Agent'), ('Admin', 'Admin'), ('RH', 'RH')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Prime',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]