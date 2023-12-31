# Generated by Django 4.2.4 on 2023-08-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_empleado_remove_conyugue_empleado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='apellido1',
            new_name='primer_apellido',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='nombre1',
            new_name='primer_nombre',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='apellido2',
            new_name='segundo_apellido',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='nombre2',
            new_name='segundo_nombre',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='correo_empresa',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='duracion_contrato',
            field=models.CharField(blank=True, choices=[('1_mes', '1 mes'), ('2_meses', '2 meses'), ('3_meses', '3 meses'), ('4_meses', '4 meses'), ('5_meses', '5 meses'), ('6_meses', '6 meses'), ('7_meses', '7 meses'), ('8_meses', '8 meses'), ('9_meses', '9 meses'), ('10_meses', '10 meses'), ('11_meses', '11 meses'), ('1_anio', '1 año'), ('2_anios', '2 años'), ('3_anios', '3 años'), ('5_anios', '5 años')], max_length=20, null=True),
        ),
    ]
