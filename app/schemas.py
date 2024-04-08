from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


class CreatePost(PostBase):
    class Config:
        from_attributes = True
