# Generated by Django 4.2.9 on 2024-02-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0010_remove_collaborateur_slaire_base_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborateur',
            name='Rémunération',
        ),
        migrations.AddField(
            model_name='collaborateur',
            name='Salaire_base',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
