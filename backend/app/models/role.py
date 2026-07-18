"""Role model for RBAC."""

from sqlalchemy import Column, String, Text, UUID as SQLUUID, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


class Role(Base, TimestampMixin):
    """Role model for role-based access control."""

    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=True, index=True
    )
    is_system_role = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Role {self.name}>"
