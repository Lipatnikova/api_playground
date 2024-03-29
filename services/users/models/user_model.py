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


class MetaModel(BaseModel):
    total: int


class UsersModel(BaseModel):
    items: List[UserModel]
    meta: MetaModel
