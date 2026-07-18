"""Organization model."""

from sqlalchemy import Column, String, Text, Boolean, Integer, UUID as SQLUUID, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Organization(Base, TimestampMixin):
    """Organization model for multi-tenancy."""

    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False, index=True)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    logo_url = Column(String(500), nullable=True)
    website = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    max_users = Column(Integer, default=10)
    max_teams = Column(Integer, default=5)

    def __repr__(self) -> str:
        return f"<Organization {self.name}>"
