"""Report model for analytics."""

from sqlalchemy import Column, String, Text, Integer, UUID as SQLUUID, ForeignKey, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Report(Base, TimestampMixin):
    """Report model for analytics and insights."""

    __tablename__ = "reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    report_type = Column(String(100), nullable=False)  # "company_research", "market_analysis", etc.
    content = Column(JSON, nullable=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True
    )
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    view_count = Column(Integer, default=0)
    is_public = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Report {self.title}>"
