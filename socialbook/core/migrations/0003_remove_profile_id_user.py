# Generated by Django 4.2.6 on 2023-10-23 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_emailverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
