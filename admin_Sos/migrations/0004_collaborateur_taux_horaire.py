# Generated by Django 4.2.9 on 2024-02-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0003_alter_collaborateur_date_d_entrée_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateur',
            name='Taux_Horaire',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
