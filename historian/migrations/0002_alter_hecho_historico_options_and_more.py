# Generated by Django 5.0 on 2023-12-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historian', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hecho_historico',
            options={'verbose_name': 'Hecho Histórico', 'verbose_name_plural': 'Hechos Históricos'},
        ),
        migrations.AlterModelOptions(
            name='personaje',
            options={'verbose_name': 'Personaje', 'verbose_name_plural': 'Personajes'},
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='fecha',
            field=models.DateField(blank=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='palabras_clave_1',
            field=models.TextField(blank=True, null=True, verbose_name='Palabra Clave 1'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='palabras_clave_2',
            field=models.TextField(blank=True, null=True, verbose_name='Palabra Clave 2'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='palabras_clave_3',
            field=models.TextField(blank=True, null=True, verbose_name='Palabra Clave 3'),
        ),
        migrations.AlterField(
            model_name='hecho_historico',
            name='resumen',
            field=models.TextField(blank=True, null=True, verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='apellido',
            field=models.CharField(blank=True, max_length=200, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='biografia',
            field=models.TextField(blank=True, null=True, verbose_name='Biografía'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='fecha_de_muerte',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Muerte'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='pais_de_origen',
            field=models.CharField(blank=True, max_length=100, verbose_name='País de Origen'),
        ),
    ]
