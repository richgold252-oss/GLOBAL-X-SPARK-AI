"""Prospect model for lead management."""

from sqlalchemy import Column, String, Text, UUID as SQLUUID, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Prospect(Base, TimestampMixin):
    """Prospect model for lead and opportunity tracking."""

    __tablename__ = "prospects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    title = Column(String(255), nullable=True)
    company_id = Column(
        UUID(as_uuid=True), ForeignKey("companies.id"), nullable=True, index=True
    )
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True
    )
    status = Column(String(50), default="new")  # new, contacted, qualified, opportunity, customer
    notes = Column(Text, nullable=True)
    is_qualified = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Prospect {self.first_name} {self.last_name}>"
