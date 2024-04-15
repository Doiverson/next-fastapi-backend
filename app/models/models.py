from sqlalchemy import Column, String, TIMESTAMP, Boolean, text
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
    published = Column(Boolean, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
