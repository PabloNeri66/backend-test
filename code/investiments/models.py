import uuid

from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from investors.models import Investor


class Investiment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(  # Invariante Estrutural
                Decimal('0.01'),
                message='Valor Mínimo = R$ 0,01',
            )
        ],
        verbose_name='Valor',
        help_text='Valor Inicial do investimento.',
    )
    investor = models.ForeignKey(
        Investor,
        on_delete=models.PROTECT,
        verbose_name='Investidor',
    )
    was_withdrawn = models.BooleanField(
        default=False,
        verbose_name='Foi retirado',
        help_text='Campo bool responsável pela a atividade do investimento.',
    )
    withdrawn_created_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Data da retirada',
        help_text='Data em que a retirada do investimento foi registrada.',
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Criado em',
        help_text='Data de criação do investimento (pode ser data passada).',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)
