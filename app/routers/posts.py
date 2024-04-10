from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from .. import schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/", response_model=List[schemas.PostBase])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost]
)
def create_post(post_create: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post_create.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return [new_post]
