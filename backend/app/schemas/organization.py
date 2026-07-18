"""Organization schemas."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class OrganizationCreate(BaseModel):
    """Organization creation request."""

    name: str = Field(..., min_length=1, max_length=255)
    slug: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    website: Optional[str] = None


class OrganizationUpdate(BaseModel):
    """Organization update request."""

    name: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None


class OrganizationResponse(BaseModel):
    """Organization response model."""

    id: uuid.UUID
    name: str
    slug: str
    description: Optional[str]
    website: Optional[str]
    is_active: bool
    max_users: int
    max_teams: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
