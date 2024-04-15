from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from ..database import get_db
from ..models import models
from ..schemas import schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


# Get all posts
@router.get("/", response_model=List[schemas.PostBase])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# Post a new post
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost]
)
def create_post(post_create: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post_create.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return [new_post]


# Delete a post
@router.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PostBase,
)
def delete_post(post_id: UUID, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db.delete(post)
    db.commit()
    return post


# Update a post
@router.put(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PostBase,
)
def update_post(
    post_id: UUID, post_update: schemas.CreatePost, db: Session = Depends(get_db)
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    post.title = post_update.title
    post.content = post_update.content
    db.commit()
    db.refresh(post)
    return post
