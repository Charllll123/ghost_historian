# Generated by Django 5.0 on 2023-12-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=200)),
                ('pais_de_origen', models.CharField(blank=True, max_length=100)),
                ('fecha_de_nacimiento', models.DateField(blank=True)),
                ('fecha_de_muerte', models.DateField(blank=True, null=True)),
                ('biografia', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hecho_Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateField(blank=True)),
                ('resumen', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('palabras_clave_1', models.TextField(blank=True, null=True)),
                ('palabras_clave_2', models.TextField(blank=True, null=True)),
                ('palabras_clave_3', models.TextField(blank=True, null=True)),
                ('personajes', models.ManyToManyField(to='historian.personaje')),
            ],
        ),
    ]
