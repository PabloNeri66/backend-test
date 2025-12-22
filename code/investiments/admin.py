from django.contrib import admin
from .models import Investiment


class InvestimentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'value', 'investor', 'created_at',
    ]
    search_fields = [
        'investor', 'cpf',
    ]


admin.site.register(Investiment, InvestimentAdmin)
