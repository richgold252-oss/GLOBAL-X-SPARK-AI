"""Permission model for RBAC."""

from sqlalchemy import Column, String, Text, UUID as SQLUUID, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base, TimestampMixin


# Association table for roles and permissions
role_permission = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", UUID(as_uuid=True), ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", UUID(as_uuid=True), ForeignKey("permissions.id"), primary_key=True),
)


class Permission(Base, TimestampMixin):
    """Permission model for fine-grained access control."""

    __tablename__ = "permissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    resource = Column(String(100), nullable=False)  # e.g., "users", "organizations"
    action = Column(String(50), nullable=False)  # e.g., "create", "read", "update", "delete"

    def __repr__(self) -> str:
        return f"<Permission {self.name}>"
