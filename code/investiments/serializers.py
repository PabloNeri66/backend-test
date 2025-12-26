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


class InvestimentWithdrawnSerializer(serializers.ModelSerializer):
    withdrawal_amount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Investiment
        fields = [
            'id',
            'created_at',
            'was_withdrawn',
            'withdrawal_amount',
            'withdrawn_created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'was_withdrawn',
            'withdrawal_amount',
        ]

    def get_withdrawal_amount(self, obj):
        investiment = InvestimentBusiness(
            obj.value,
            obj.created_at,
            obj.withdrawn_created_at,
        )
        return investiment.calculate_net_amount_withdrawn()

    def validate(self, attrs):
        withdrawn_date = attrs.get('withdrawn_created_at')
        now = timezone.now()

        if self.instance.was_withdrawn:
            raise serializers.ValidationError(
                'Este investimento já foi resgatado.'
            )

        if withdrawn_date:
            if withdrawn_date > now:
                raise serializers.ValidationError({
                    'withdrawn_created_at': 'Data Futura não permitida.'
                })

            if withdrawn_date < self.instance.created_at:
                raise serializers.ValidationError({
                    'withdrawn_created_at':
                    'Data não pode ser anterior à criação do investimento.'
                })

        return attrs

    def update(self, instance, validated_data):
        now = timezone.now()
        withdrawn_date = validated_data.get('withdrawn_created_at')

        instance.withdrawn_created_at = withdrawn_date or now

        instance.was_withdrawn = True
        instance.save()
        return instance
