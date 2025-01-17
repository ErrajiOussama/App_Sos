# Generated by Django 4.2.9 on 2024-02-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0057_alter_collaborateur_n_cin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Activite',
            field=models.CharField(blank=True, choices=[('FRANCE', 'FRANCE'), ('CANADA', 'CANADA')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='CSP',
            field=models.CharField(blank=True, choices=[('AGENT', 'AGENT'), ('CADRE', 'CADRE'), ('TECHNICIEN', 'TECHNICIEN'), ('STAGIAIRE', 'STAGIAIRE')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Declaration_CNSS',
            field=models.CharField(blank=True, choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_CNSS',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_Passeport',
            field=models.CharField(blank=True, default='-', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_de_téléphone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Nationalité',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Nom',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Poste',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Prenom',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='RIB',
            field=models.CharField(blank=True, default='-', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Sexe',
            field=models.CharField(blank=True, choices=[('H', 'H'), ('F', 'F')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Type_de_contrat',
            field=models.CharField(blank=True, choices=[('Etranger', 'Etranger'), ('Stage', 'Stage'), ('CDD', 'CDD'), ('CDI', 'CDI')], max_length=100, null=True),
        ),
    ]
