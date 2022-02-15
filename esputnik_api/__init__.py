__version__ = "0.0.1"

import typing
from urllib.parse import urljoin

import requests

from esputnik_api.schema import VersionSchema, AccountInfoSchema, SendEmailResultSchema


class ESputnik:
    base_url = 'https://esputnik.com/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def version(self) -> typing.Optional[VersionSchema]:
        response = requests.get(
            url=urljoin(self.base_url, '/api/v2/version'),
            auth=('api-user', self.api_key)
        )
        response.raise_for_status()
        return VersionSchema(**response.json())

    def account_info(self) -> AccountInfoSchema:
        response = requests.get(
            url=urljoin(self.base_url, '/api/v1/account/info'),
            auth=('api-user', self.api_key)
        )
        response.raise_for_status()
        return AccountInfoSchema(**response.json())

    def send_mail(
            self, from_: str, to: typing.List[str], subject: str, html_text: str
    ) -> typing.List[SendEmailResultSchema]:
        payload = {
            'from': from_,
            'emails': to,
            'subject': subject,
            'htmlText': html_text,
        }
        response = requests.post(
            url=urljoin(self.base_url, '/api/v1/message/email'),
            json=payload,
            auth=('api-user', self.api_key)
        )
        response.raise_for_status()
        results = response.json()['results']
        if isinstance(results, dict):
            results = [results]
        return [SendEmailResultSchema(**e) for e in results]
