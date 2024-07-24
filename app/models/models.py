from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base
import uuid


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = Column(String, index=True)
    content = Column(String, nullable=False)
    details = relationship("Detail", back_populates="post")  # Corrected relationship


class Detail(Base):
    __tablename__ = "details"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    description = Column(String, nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id"))
    post = relationship("Post", back_populates="details")
