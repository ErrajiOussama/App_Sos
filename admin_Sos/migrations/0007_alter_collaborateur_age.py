# Generated by Django 4.2.9 on 2024-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0006_remove_collaborateur_rémunération_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='Age',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
