from django.db import models
from django.core.validators import RegexValidator
from django.db.models import CASCADE
from django.db.models.fields import DateTimeField

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=40, unique=True)
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)

    def __str__(self):
        return f"{self.customer_name}"


class ServiceRepresentative(models.Model):
    service_rep_id = models.IntegerField(primary_key=True)
    service_rep_name = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    start_date = models.DateTimeField(editable=True)
    specialization = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.service_rep_name}"
  

class SupportTicket(models.Model):
  COMPL_STATUS = [
     ('Pending', 'Pending'),
     ('In Progress', 'In Progress'),
     ('Completed', 'Completed'),
     ('Cancelled', 'Cancelled'),
  ]
  ticket_id = models.IntegerField(primary_key=True)
  model_name = models.CharField(max_length=80)
  model_number = models.IntegerField()
  scope_of_work = models.TextField(max_length=1000)
  ticket_creation_timestamp = models.DateTimeField(auto_created=True)
  customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
  service_rep_id = models.ForeignKey(ServiceRepresentative, on_delete=models.RESTRICT)
  service_rep_notes = models.TextField(max_length=1000)
  repair_completion = models.CharField(choices=COMPL_STATUS, max_length=20, default='pending')

  def __str__(self):
     return f"{self.ticket_id}"
  

class HistTicketRecord(models.Model):
  ticket_id = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
  service_rep_id = models.ForeignKey(ServiceRepresentative, on_delete=models.RESTRICT)
  ticket_assigned_timestamp = models.DateTimeField(editable=True)
  ticket_completion_timestamp = models.DateTimeField(editable=True)

  def __str__(self):
    return f"{self.ticket_id}"


