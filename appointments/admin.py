from django.contrib import admin

# Register your models here.

from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('name','phone','preferred_date','status')

    list_filter = ('status',)

    search_fields = ('name','phone')

admin.site.register(Appointment,AppointmentAdmin)