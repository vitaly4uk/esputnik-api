import typing
from enum import Enum

from pydantic import BaseModel, Field, EmailStr

class SendEmailStatus(Enum):
    ok: str = 'OK'
    error: str = 'ERROR'

class VersionSchema(BaseModel):
    version: str
    protocol_version: str = Field(alias='protocolVersion')


class AccountInfoSchema(BaseModel):
    user_email: EmailStr = Field(alias='userEmail')
    organisation_name: str = Field(alias='organisationName')


class SendEmailResultSchema(BaseModel):
    locator: str
    status: SendEmailStatus
    request_id: str = Field(alias='requestId')
    message: typing.Optional[str] = None

    class Config:
        use_enum_values = True
