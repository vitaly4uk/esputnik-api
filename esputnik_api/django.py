import typing

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail.backends.base import BaseEmailBackend

from esputnik_api import ESputnik


class ESputnikEmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages: typing.List[EmailMessage]):
        esputnik = ESputnik(api_key=settings.ESPUTNIK_API_KEY)
        for message in email_messages:
            esputnik.send_mail(
                from_=message.from_email,
                to=message.to,
                subject=message.subject,
                html_text=message
            )
