# Generated by Django 5.0.6 on 2024-05-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
            ],
        ),
    ]
