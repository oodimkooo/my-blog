from django.contrib import admin

from .models import quotesMain


class QuotesAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "publisher", "date_published")
    search_fields = ("author","publisher")

admin.site.register(quotesMain,QuotesAdmin)
# Register your models here.
