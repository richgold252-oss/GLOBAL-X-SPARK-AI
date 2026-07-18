"""API Key model for service authentication."""

from sqlalchemy import Column, String, UUID as SQLUUID, ForeignKey, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base, TimestampMixin


class APIKey(Base, TimestampMixin):
    """API Key model for service-to-service authentication."""

    __tablename__ = "api_keys"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    key = Column(String(255), unique=True, nullable=False, index=True)
    hashed_key = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=True, index=True
    )
    is_active = Column(Boolean, default=True, index=True)
    last_used_at = Column(DateTime, nullable=True)
    expires_at = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<APIKey {self.name}>"
