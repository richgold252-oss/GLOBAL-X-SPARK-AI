"""Company model for BI."""

from sqlalchemy import Column, String, Text, Integer, UUID as SQLUUID, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Company(Base, TimestampMixin):
    """Company model for business intelligence."""

    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False, index=True)
    website = Column(String(500), nullable=True)
    industry = Column(String(100), nullable=True)
    size = Column(String(50), nullable=True)  # "startup", "small", "medium", "enterprise"
    logo_url = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True
    )
    research_count = Column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<Company {self.name}>"
