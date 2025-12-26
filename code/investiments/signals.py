import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from .models import Investiment
from services.investiments import InvestimentService

logger = logging.getLogger(__name__)
investiment_service = InvestimentService()


@receiver(post_save, sender=Investiment)
def send_investiment_created_event(sender, instance, created, **kwargs):
    try:
        if created:
            data = dict(
                event_type='create-investiment',
                investiment_id=instance.id,
                value=instance.value,
                investor=instance.investor,
                timestamp_created_at=timezone.localtime(
                    instance.created_at
                ).strftime("%Y/%m/%d, %H:%M:%S"),
            )

            investiment_service.send_created_investiment_email(data=data)
            logger.info(f'enviando Ok! {data.get('timestamp_created_at')}')

    except Exception as e:
        logger.error(f"[ERRO SIGNAL Investiment-create] {e}")
        pass
