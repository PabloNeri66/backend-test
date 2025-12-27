import os
from django.core.mail import EmailMessage


class InvestimentService:
    def send_created_investiment_email(self, data):
        email = self._investiment_created_build(data=data)
        email.send()

    def _investiment_created_build(self, data):
        EMAILTO = os.getenv('EMAILTO')

        subject = f'Investimento nº{data.get("investiment")} criado :)'

        body = (
            f'Valor do investimento: {data.get("value")}\n'
            f'Investidor: {data.get("investor")}\n'
            f'Data: {data.get("timestamp_created_at")}'
        )

        email = EmailMessage(
            subject=subject,
            body=body,
            to=[EMAILTO],
        )

        return email
