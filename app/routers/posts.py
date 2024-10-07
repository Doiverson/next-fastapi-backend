from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
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
    try:
        posts = db.query(models.Post).all()
        return posts
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Post a new post
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.CreatePost
)
def create_post(post_create: schemas.CreatePost, db: Session = Depends(get_db)):
    try:
        new_post = models.Post(**post_create.dict(exclude={"detail"}))
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        
        new_detail = models.Detail(
              post_id=new_post.id, 
              title=post_create.title, 
              description=post_create.description
            )
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)            

        return post_create  # Return the newly created post

    except Exception as e:
        db.rollback()  # Rollback the session in case of an error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Delete a post
@router.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PostBase,
)
def delete_post(post_id: UUID, db: Session = Depends(get_db)):
    try:
        post = db.query(models.Post).filter(models.Post.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        db.delete(post)
        db.commit()
        return post
    except Exception as e:
        db.rollback()  # Rollback the session in case of an error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Update a post
@router.put(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PostBase,
)
def update_post(
    post_id: UUID, post_update: schemas.CreatePost, db: Session = Depends(get_db)
):
    try:
        post = db.query(models.Post).filter(models.Post.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        post.title = post_update.title
        post.content = post_update.content
        db.commit()
        db.refresh(post)
        return post
    except Exception as e:
        db.rollback()  # Rollback the session in case of an error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
