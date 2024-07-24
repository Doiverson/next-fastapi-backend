from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from ..database import get_db
from ..models import models
from ..schemas import schemas

router = APIRouter(
    prefix="/details",
    tags=["Details"],
)


# Get all details
@router.get("/", response_model=List[schemas.DetailBase])
def get_details(db: Session = Depends(get_db)):
    details = db.query(models.Detail).all()
    return details


# Get a detail by id
@router.get("/{post_id}", response_model=schemas.DetailBase)
def get_detail(post_id: UUID, db: Session = Depends(get_db)):
    detail = (
        db.query(models.Detail)
        .join(models.Post)
        .filter(models.Post.id == post_id)
        .first()
    )
    return detail


# Post a new detail
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateDetail
)
def create_detail(post_detail: schemas.CreateDetail, db: Session = Depends(get_db)):

    existing_detail = (
        db.query(models.Detail)
        .filter(models.Detail.post_id == post_detail.post_id)
        .first()
    )

    if existing_detail:
        # Update the existing detail
        existing_detail.description = post_detail.description
        db.commit()
        db.refresh(existing_detail)
        return existing_detail
    else:
        # Create a new detail
        new_detail = models.Detail(**post_detail.dict())
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        return new_detail


# Delete a detail
@router.delete(
    "/{detail_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.DetailBase,
)
def delete_detail(detail_id: UUID, db: Session = Depends(get_db)):
    detail = db.query(models.Detail).filter(models.Detail.id == detail_id).first()
    db.delete(detail)
    db.commit()
    return detail


# Edit a detail
@router.put(
    "/{detail_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.DetailBase,
)
def update_detail(
    detail_id: UUID, detail_update: schemas.UpdateDetail, db: Session = Depends(get_db)
):
    detail = db.query(models.Detail).filter(models.Detail.id == detail_id).first()
    detail.description = detail_update.description
    db.commit()
    db.refresh(detail)
    return detail
