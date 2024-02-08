# Generated by Django 4.2.9 on 2024-02-08 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_Sos', '0017_rename_log_collaborateur_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborateur',
            name='password',
        ),
        migrations.RemoveField(
            model_name='collaborateur',
            name='username',
        ),
        migrations.AddField(
            model_name='collaborateur',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]