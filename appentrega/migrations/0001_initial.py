# Generated by Django 5.0.2 on 2024-02-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=20)),
                ('trabajo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rubro', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro', models.CharField(max_length=40)),
                ('puesto', models.CharField(max_length=20)),
            ],
        ),
    ]