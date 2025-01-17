# Generated by Django 4.2.9 on 2024-02-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0038_alter_collaborateur_n_passeport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Adresse_postale',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Commentaire',
            field=models.CharField(blank=True, default='-', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='E_mail',
            field=models.EmailField(blank=True, default='-', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Motif_de_départ',
            field=models.CharField(blank=True, choices=[('Demission', 'Demission'), ('Licenciement', 'Licenciement'), ('FPE', 'FPE'), ('Fin de contrat', 'Fin de contrat'), ('Comportement', 'Comportement'), ('Etudes', 'Etudes'), ('Sans motif(Volantaire)', 'Sans motif(Volantaire)')], default='-', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_CIN',
            field=models.CharField(blank=True, default='-', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='N_CNSS',
            field=models.CharField(blank=True, default='-', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Nationalité',
            field=models.CharField(blank=True, default='-', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Nombre_d_enfants',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='RIB',
            field=models.CharField(blank=True, default='-', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='S_H',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='Ville',
            field=models.CharField(blank=True, default='-', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='anciennetee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='salaire_finale',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
