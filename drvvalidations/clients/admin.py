from django.contrib import admin


from clients.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'rg', 'phone', 'is_active')
    search_fields = ('name', 'email', 'cpf', 'rg', 'phone', 'is_active')
    list_filter = ('name', 'email', 'cpf', 'rg', 'phone', 'is_active')
