from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='investors',
        verbose_name='Investidores',
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Nome',
    )
    cpf = models.CharField(
        max_length=15,
        verbose_name='CPF',
    )

    def __str__(self):
        return str(self.pk)
