from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'email', 'create_date')
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name',
    list_display_links = 'id', 'phone'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',