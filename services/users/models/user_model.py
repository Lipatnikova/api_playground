import re
from typing import List

from pydantic import BaseModel, UUID4, field_validator


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: UUID4

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

    @field_validator("email")
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
            raise ValueError("Email is invalid")
        return value


class MetaModel(BaseModel):
    total: int


class UsersModel(BaseModel):
    items: List[UserModel]
    meta: MetaModel
