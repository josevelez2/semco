# Generated by Django 4.2.5 on 2023-10-08 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_empleado_documentos_de_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='de_quien_depende',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleados_subordinados', to='pages.empleado'),
        ),
    ]
