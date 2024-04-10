from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
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
