# Generated by Django 4.2.5 on 2023-09-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0003_alter_ticketmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmodel',
            name='priority',
            field=models.CharField(default='N', max_length=20),
        ),
    ]