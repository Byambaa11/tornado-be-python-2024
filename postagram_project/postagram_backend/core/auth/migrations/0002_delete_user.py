# Generated by Django 5.0 on 2024-03-13 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_auth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
