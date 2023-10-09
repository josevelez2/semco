# Generated by Django 4.2.5 on 2023-10-05 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0008_alter_ticketmodel_assignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='assignedto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedto', to=settings.AUTH_USER_MODEL),
        ),
    ]