# Generated by Django 5.0.6 on 2024-05-09 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='age',
        ),
    ]
