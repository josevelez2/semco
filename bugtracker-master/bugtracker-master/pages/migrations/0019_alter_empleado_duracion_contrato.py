# Generated by Django 4.2.5 on 2023-09-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_rename_jefe_inmediato_empleado_persona_a_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='duracion_contrato',
            field=models.CharField(blank=True, choices=[('3_meses', '3 meses'), ('6_meses', '6 meses'), ('1_anio', '1 año')], max_length=20, null=True),
        ),
    ]
