# Django Support Ticket System Objects Setup
### Example Data submitted through the ORM shell.
#### Script/s for inserting objects into the Postgres DB, from the Django ORM shell.

```python REPL
from tickets.models import Customer

cust1 = Customer(customer_name='Alice Smith', street='123 Maple St', city='Los Angeles', state='California', country='USA', phone='555-0192', email='alice.smith@example.com')
cust1.save()

cust2 = Customer(customer_name='Bob Jones', street='456 Oak Ave', city='New York', state='New York', country='USA', phone='555-0143', email='bob.jones@example.com')
cust2.save()

cust3 = Customer(customer_name='Charlie Brown', street='789 Pine Rd', city='Toronto', state='Ontario', country='Canada', phone='555-0177', email='charlie.b@example.com')
cust3.save()

cust4 = Customer(customer_name='Diana Prince', street='101 Gateway Blvd', city='London', state='England', country='UK', phone='555-0188', email='diana.p@example.com')
cust4.save()

cust1.pk

Customer.objects.get(pk=1)
Customer.objects.all()
Customer.objects.filter(state='California')
Customer.objects.get(email='alice.smith@example.com')

```
### Now ORM relationships
 Service Reps, support tickets and customers.  
 * Create one ServiceRepresentative object
 * Save it 
 * Create one SupportTicket for Customer 'Alice Smith' 
 * Assign the Rep and Cust to the ticket through the ForeignKey fields.
 
```python REPL
srep1 = ServiceRepresentative(service_rep_id=369, service_rep_name='Jimmy Pops', phone='(123) 555-9001', email='jpops9@support.com', start_date='2024-01-15', specialization='Electrical Shorts and Faulty wiring schemas')
srep1.save()

srep2 = ServiceRepresentative(service_rep_id=12, service_rep_name='Janie Silverson', phone='(123) 555-1012', email='jsilverson1@support.com', start_date='1998-08-27', specialization='Software configurations, embedded systems, and assembly language')
srep2.save()

srep3 = ServiceRepresentative(service_rep_id=181, service_rep_name='Alex Wong', phone='(123) 555-7134', email='awong1@support.com', start_date='2013-05-13', specialization='Networks, systems administration, network connectivity')
srep3.save()

ServiceRepresentative.objects.all()

customerfk = Customer.objects.get(customer_name='Alice Smith')
service_repfk = ServiceRepresentative.objects.get(service_rep_name='Jimmy Pops')

stick1 = SupportTicket(model_name='QuantumBook Pro', model_number='QB-2026x', scope_of_work='Screen flickering and intermittent power failure.', customer=customerfk, service_rep=service_repfk, service_rep_notes='Replaced the display cable. Power issue resolved after firmware flash.', repair_status='Completed', ticket_completed_at=datetime(2026, 8, 20, 9, 15, 0, tzinfo=ZoneInfo("America/New_York")),)
stick1.save()


customerfk2 = Customer.objects.get(customer_name='Diana Prince')
service_repfk2 = ServiceRepresentative.objects.get(service_rep_name='Alex Wong')

stick2 = SupportTicket(model_name='SpeedRoute 5G', model_number='SR-500', scope_of_work='Router drops Wi-Fi signals every 20 minutes.', customer=customerfk2, service_rep=service_repfk2, service_rep_notes='Monitoring signal strength. Suspicion of overheating hardware.', repair_status='In Progress', ticket_completed_at=datetime(2026, 8, 21, 14, 30, 0, tzinfo=ZoneInfo("America/New_York")),)
stick2.save()


customerfk3 = Customer.objects.get(customer_name='Charlie Brown')
service_repfk3 = ServiceRepresentative.objects.get(service_rep_name='Janie Silverson')

stick3 = SupportTicket(model_name='CyrptoMine Pro 9000', model_number='CMP-9000b', scope_of_work='Shutdown with Error: Missing critical algorithms/files.', customer=customerfk3, service_rep=service_repfk3, service_rep_notes='Remote pull of all error codes and customer keystrokes', repair_status='In Progress', ticket_completed_at=datetime(2026, 8, 22, 16, 5, 0, tzinfo=ZoneInfo("America/New_York")),)
stick3.save()


customerfk4 = Customer.objects.get(customer_name='Bob Jones')

stick4 = SupportTicket(model_name='GameFlight FXX', model_number='GFFXX3', scope_of_work='Cannot access gameportals, Minecraft Builder World, or most of the other Online Gaming logins.', customer=customerfk4,)
stick4.save()


customerfk5 = Customer.objects.get(customer_name='Charlie Brown')
service_repfk5 = ServiceRepresentative.objects.get(service_rep_name='Jimmy Pops')

stick5 = SupportTicket(model_name='QuantumBook Pro', model_number='QB-2026X', scope_of_work='Customer reports getting an electrical shock everytime he visits any Ai websites, i.e. Google Gemini, Anthropic Claude, or Meta Llama', customer=customerfk5, service_rep=service_repfk5, service_rep_notes='I was just assigned this ticket, will update once I investagate more.', repair_status='In Progress',)
stick5.save()

SupportTicket.objects.all()

```
### The code that follows is to correct an SupportTicket Object,
### if you entered an object with out the Timezone value or to make the object Timezone aware.

```python REPL
from datetime import datetime
from zoneinfo import ZoneInfo
from tickets.models import SupportTicket

stick1 = SupportTicket.objects.get(pk=1)

intended_time = datetime(
    2026, 8, 20, 9, 15, 0,
    tzinfo=ZoneInfo("America/New_York")
)

stick1.ticket_completed_at = intended_time
stick1.save(update_fields=["ticket_completed_at"])

print(stick1.ticket_completed_at)
print(timezone.localtime(stick1.ticket_completed_at))

supticket = SupportTicket.objects.get(pk=1)

print(supticket.ticket_completed_at)
print("Customer:", supticket.customer, "Customer ID:", supticket.customer_id, "Service Rep:", supticket.service_rep, "Service Rep ID:", supticket.service_rep_id)

```
## Quering through/with Relationships
 Using Forgein Key with join and relationship lookups using Django's double-underscore syntax, etc.
* FROM = LEFT
* JOIN = RIGHT

```python REPL

SupportTicket.objects.filter(customer__state = 'California')

Customer.objects.values_list('customer_id', 'customer_name', 'state', 'country')

ServiceRepresentative.objects.values_list('service_rep_id', 'service_rep_name', 'specialization')

SupportTicket.objects.values_list('ticket_id', 'model_name', 'customer_id', 'service_rep_id', 'repair_status')

```

