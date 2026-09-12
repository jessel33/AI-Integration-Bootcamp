from django.contrib import admin

from .models import Customer, ServiceRepresentative, SupportTicket


class SupportTicketAdmin(admin.ModelAdmin):
    list_display = (
        "ticket_id",
        "model_number",
        "scope_of_work",
        "customer",
        "service_rep",
        "repair_status",
        "ticket_completed_at",
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "street",
        "city",
        "state",
        "country",
        "phone",
        "email",
    )


class ServiceRepresentativeAdmin(admin.ModelAdmin):
    list_display = (
        "service_rep_id",
        "service_rep_name",
        "phone",
        "email",
        "start_date",
        "specialization",
    )


admin.site.register(SupportTicket, SupportTicketAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ServiceRepresentative, ServiceRepresentativeAdmin)
