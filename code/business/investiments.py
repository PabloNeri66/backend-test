import datetime
from decimal import ROUND_HALF_EVEN, Decimal
from typing import Optional

from django.utils import timezone


class InvestimentBusiness:
    '''Lógica de Negócio do Investimento

    O investimento renderá 0,52% todos os meses,
    no mesmo dia em que for realizado.
    Dado que o ganho é pago mensalmente, deve ser tratado como ganho composto,
    o que significa que a cada novo período (mês)
    o valor ganho passará a fazer parte do saldo do investimento para
    o próximo pagamento.

    '''
    MONTHLY_RATE = Decimal('0.0052')

    def __init__(
        self,
        investiment_value: Decimal,
        investiment_created_at: datetime.datetime,
        withdrawn_created_at: Optional[datetime.datetime] = None,
    ):
        self.investiment_value = investiment_value
        self.investiment_created_at = investiment_created_at
        self.withdrawn_created_at = withdrawn_created_at

    def calculate_amount(self) -> Decimal:
        '''
        Calculo do Montante de um investimento aberto(data atual).
        '''
        initial_date = self.investiment_created_at.date()
        today = timezone.localdate()

        months = self._full_months_between(initial_date, today)
        amount = (
            self.investiment_value
            * (  # Juros composto
                Decimal('1') + self.MONTHLY_RATE
            )
            ** months
        )

        return amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

    def calculate_gains(self) -> Decimal:
        '''
        Cálculo dos ganhos (montante - investido) em um investimento
        aberto(Data atual).
        '''
        amount = self.calculate_amount()
        gains = amount - self.investiment_value

        return gains.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

    def calculate_amount_withdrawn(self) -> Decimal:
        '''
        Saldo Montante em um investimento fechado.
        '''
        initial_date = self.investiment_created_at.date()
        withdrawn_date = self.withdrawn_created_at.date()

        months = self._full_months_between(initial_date, withdrawn_date)

        amount = (
            self.investiment_value
            * (Decimal('1') + self.MONTHLY_RATE) ** months
        )

        return amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

    def calculate_gains_withdrawn(self) -> Decimal:
        '''Calculo de Ganho em um investimento Fechado.'''
        amount = self.calculate_amount_withdrawn()
        gains = amount - self.investiment_value

        return gains.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

    def calculate_net_amount_withdrawn(self):
        '''
        Calculo do montante para saque de um investimento fechado
        (A tributar os ganhos).

        Se tiver menos de um ano, a percentagem será de **22,5%** (imposto = 45,00).
        Se tiver entre um e dois anos, a percentagem será de **18,5%** (imposto = 37,00).
        Se tiver mais de dois anos, a percentagem será de **15%** (imposto = 30,00).
        '''
        amount = self.calculate_amount_withdrawn()
        gains = amount - self.investiment_value
        initial_date = self.investiment_created_at.date()
        withdrawn_date = self.withdrawn_created_at.date()

        TAX_UNDER_12 = Decimal('0.225')
        TAX_12_TO_24 = Decimal('0.185')
        TAX_OVER_24 = Decimal('0.15')

        months = self._full_months_between(initial_date, withdrawn_date)

        if months < 12:
            gains_tax = gains * TAX_UNDER_12
        elif months > 24:
            gains_tax = gains * TAX_OVER_24
        else:
            gains_tax = gains * TAX_12_TO_24

        return (amount - gains_tax).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_EVEN
        )  # saldo montante(amount) limpo para retorno.

    def calculate_net_gains_withdrawn(self) -> Decimal:
        '''
        Calculo dos Ganhos de um investimento fechado e tributado.
        '''
        amount = self.calculate_net_amount_withdrawn()
        initial_investiment = self.investiment_value

        return (amount - initial_investiment).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_EVEN
        )

    def _full_months_between(self, start, end):
        '''
        Calcula a quantidade de meses **inteiros** entre duas datas.

        Um mês só é contabilizado se o período completar um ciclo mensal cheio,
        isto é, o dia do mês em `end` deve ser maior ou = dia em `start`.

        Regra de negócio:
        - Meses parciais não são considerados.
        - A contagem só avança quando o mês seguinte é completado.

        exemplo: 12/09 -> 11/10 = 0 meses;
        '''
        months = (end.year - start.year) * 12 + (end.month - start.month)
        if end.day < start.day:
            months -= 1
        return max(months, 0)
