"""Team model."""

from sqlalchemy import Column, String, Text, Integer, UUID as SQLUUID, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Team(Base, TimestampMixin):
    """Team model for grouping users."""

    __tablename__ = "teams"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True
    )
    lead_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    max_members = Column(Integer, default=50)

    def __repr__(self) -> str:
        return f"<Team {self.name}>"
