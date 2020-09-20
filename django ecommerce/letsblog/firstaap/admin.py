from django.contrib import admin
from .form import SignUpForm, ProductEntry
# Register your models here.


@admin.register(ProductEntry)
class ProductEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'productname']
