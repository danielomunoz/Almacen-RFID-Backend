# Generated by Django 4.1.7 on 2023-04-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_accion_fecha_alter_objeto_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='codigo_rfid',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='imagen',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='movil',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
