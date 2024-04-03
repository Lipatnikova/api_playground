from typing import List

from pydantic import BaseModel, UUID4, field_validator


class WishlistItemModel(BaseModel):
    title: str
    uuid: UUID4

    @field_validator("title", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class WishlistItemsModel(BaseModel):
    items: List[WishlistItemModel]
    user_uuid: UUID4



