from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("pk","title","startDate","endDate")
    search_fields = ("title",)

admin.site.register(Event,EventAdmin)
