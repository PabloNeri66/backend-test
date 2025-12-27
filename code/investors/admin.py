from django.contrib import admin
from .models import Investor


class InvestorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'cpf']
    search_fields = [
        'cpf',
    ]


admin.site.register(Investor, InvestorAdmin)
