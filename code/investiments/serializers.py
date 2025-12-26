from rest_framework import serializers
from django.utils import timezone

from business.investiments import InvestimentBusiness
from .models import Investiment


class InvestimentListSerializer(serializers.ModelSerializer):
    balance_amount = serializers.SerializerMethodField()
    gains = serializers.SerializerMethodField()

    class Meta:
        model = Investiment
        fields = [
            'id',
            'investor',
            'value',
            'gains',
            'created_at',
            'balance_amount',
            'was_withdrawn',
            'withdrawn_created_at',
            'updated_at',
        ]

    def _business(self, obj):
        '''
        Reaproveita o código Classe das regras de negócio para atribuir
        no objeto em instância -> Investimento.
        '''
        if not hasattr(obj, '_business_cache'):
            obj._business_cache = InvestimentBusiness(
                investiment_value=obj.value,
                investiment_created_at=obj.created_at,
                withdrawn_created_at=obj.withdrawn_created_at,
            )
        return obj._business_cache

    def get_gains(self, obj):
        business = self._business(obj)

        if obj.withdrawn_created_at:
            return business.calculate_gains_withdrawn()

        return business.calculate_gains()

    def get_balance_amount(self, obj):
        business = self._business(obj)

        if obj.withdrawn_created_at:
            return business.calculate_amount_withdrawn()

        return business.calculate_amount()


class InvestimentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investiment
        fields = [
            'id',
            'created_at',
            'investor',
            'value',
        ]
        read_only_fields = [
            'id',
        ]
        extra_kwargs = {
            'value': {'write_only': True}
        }

    def validate_created_at(self, value):
        if value > timezone.now():
            raise serializers.ValidationError({'Data futura não é permitida.'})
        return value
