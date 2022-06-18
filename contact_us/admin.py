from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'subject',
        'message',
    )

    ordering = ('email',)

admin.site.register(ContactUs, ContactUsAdmin)
