# En bugtracker_app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from bugtracker_project.settings import AUTH_USER_MODEL

class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.username

class TicketModel(models.Model):
    title = models.CharField(max_length=100, default=None)
    datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(default=None)
    ticketfiler = models.ForeignKey(
        AUTH_USER_MODEL, related_name='ticketfiler',
        on_delete=models.CASCADE, default=None)

    NEW = "N"
    INPROGRESS = "INP"
    DONE = "D"
    INVALID = "INV"
    APPROVED = "APR"
    DENIED = "DEN"

    TICKET_STATUS_CHOICES = [
        (NEW, 'New'),
        (INPROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    ]

    status = models.CharField(
        max_length=3, choices=TICKET_STATUS_CHOICES, default=NEW)

    assignedto = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignedto',
        blank=True,
        null=True,
        default=None)
    completedby = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='completedby',
        blank=True,
        null=True,
        default=None)

    priority = models.CharField(max_length=20, default='N')

    def __str__(self):
        return self.title

assignedto = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_tickets',
        blank=True,
        null=True,
        default=None)

