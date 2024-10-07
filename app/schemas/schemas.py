from pydantic import BaseModel
from uuid import UUID


class PostBase(BaseModel):
    id: UUID
    title: str
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Example Title",
                "description": "Example Description",
            }
        }


class CreatePost(BaseModel):
    title: str
    description: str
    detail: 'CreateDetail'

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
              "title": "Example Title", 
              "description": "Example Description",
              "detail": {
                "description": "Example Descriptino",
              }
            }
        }


class DetailBase(BaseModel):
    id: UUID
    title: str
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Title",
                "description": "Example Description",
            }
        }


class CreateDetail(BaseModel):
    tags: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "tags": "Example Description",
                "post_id": "cc6f1c59-05ae-4f88-a04c-b5ce7d3d92a8",
            }
        }


class UpdateDetail(BaseModel):
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "description": "Example Description",
            }
        }
