# Generated by Django 4.2.5 on 2023-10-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectotf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe_tf',
            name='observaciones',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto_tf',
            name='observaciones',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
