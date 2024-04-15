from pydantic import BaseModel
from uuid import UUID


class PostBase(BaseModel):
    id: UUID
    title: str
    content: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Example Title",
                "content": "Example Content",
            }
        }


class CreatePost(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {"title": "Example Title", "content": "Example Content"}
        }
