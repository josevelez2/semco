# Generated by Django 4.2.3 on 2023-08-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_registroempleados2_estado_civil'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroempleados2',
            name='empresa_temporal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='registroempleados2',
            name='duracion_contrato',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
