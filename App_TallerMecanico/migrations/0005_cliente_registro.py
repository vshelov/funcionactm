# Generated by Django 5.0 on 2024-11-07 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_TallerMecanico', '0004_cliente_datos_completos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='registro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_TallerMecanico.registro'),
        ),
    ]
