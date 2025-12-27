from decimal import Decimal
from django.utils import timezone
from datetime import datetime
from django.test import TestCase
from business.investiments import InvestimentBusiness


class InvestimentBusinessOpenTest(TestCase):
    def setUp(self):
        self.investiment = make_investiment(
            value=Decimal('1000'),
            created_at=timezone.make_aware(datetime(2025, 11, 13, 0, 0)),
            withdrawn_at=timezone.make_aware(datetime(2025, 12, 12, 0, 0)),
        )

    def test_calculate_amount_is_equal(self):
        self.assertEqual(
            self.investiment.calculate_amount(), Decimal('1005.20')
        )

    def test_calculate_gains_is_equal(self):
        self.assertEqual(self.investiment.calculate_gains(), Decimal('5.20'))


class InvestimentBusinessWithdrawnTest(TestCase):
    def setUp(self):
        self.investiment = make_investiment(
            value=Decimal('1000'),
            created_at=timezone.make_aware(datetime(2025, 11, 13, 0, 0)),
            withdrawn_at=timezone.make_aware(datetime(2025, 12, 12, 0, 0)),
        )

    def test_calculate_amount_withdrawn_is_equal(self):
        self.assertEqual(
            self.investiment.calculate_amount_withdrawn(), Decimal('1000.00')
        )

    def test_calculate_gains_withdrawn_is_equal(self):
        self.assertEqual(
            self.investiment.calculate_gains_withdrawn(), Decimal('0')
        )


class InvestimentBusinessNetWithdrawnTest(TestCase):
    def setUp(self):
        self.investiment = make_investiment(
            value=Decimal('1000'),
            created_at=timezone.make_aware(datetime(2025, 11, 13, 0, 0)),
            withdrawn_at=timezone.make_aware(datetime(2025, 12, 12, 0, 0)),
        )

    def test_calculate_net_amount_withdrawn_is_equal(self):
        self.assertEqual(
            self.investiment.calculate_net_amount_withdrawn(), Decimal('1000')
        )

    def test_calculate_net_gains_withdrawn_is_equal(self):
        self.assertEqual(
            self.investiment.calculate_net_gains_withdrawn(), Decimal('0')
        )


def make_investiment(*, value='1000.00', created_at, withdrawn_at=None):
    """Top-Level Construtora da classe de testes"""
    return InvestimentBusiness(
        investiment_value=Decimal(value),
        investiment_created_at=created_at,
        withdrawn_created_at=withdrawn_at,
    )
