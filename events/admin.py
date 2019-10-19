from django.contrib import admin

from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'start_date_time', 'end_date_time')
