# Generated by Django 4.2.9 on 2024-02-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0026_collaborateur_anciennetee'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateur',
            name='Commentaire',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]