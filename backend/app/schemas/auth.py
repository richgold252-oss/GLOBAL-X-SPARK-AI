"""Authentication schemas."""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid


class TokenResponse(BaseModel):
    """Token response model."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class RegisterRequest(BaseModel):
    """User registration request."""

    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None


class LoginRequest(BaseModel):
    """User login request."""

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """User response model."""

    id: uuid.UUID
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class APIKeyRequest(BaseModel):
    """API Key generation request."""

    name: str = Field(..., min_length=1, max_length=255)


class APIKeyResponse(BaseModel):
    """API Key response model."""

    id: uuid.UUID
    name: str
    key: str  # Only shown on creation
    created_at: datetime

    class Config:
        from_attributes = True
