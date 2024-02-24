from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'year', 'image_tag']
    # readonly_fields = ['image_tag',]
    list_filter = ['author', 'year']