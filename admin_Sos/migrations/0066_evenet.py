# Generated by Django 4.2.9 on 2024-04-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_Sos', '0065_rh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]