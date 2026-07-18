"""Database connection and session management."""

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool, QueuePool
from app.core.config import get_settings
import logging


logger = logging.getLogger(__name__)
settings = get_settings()


def get_engine() -> Engine:
    """Create SQLAlchemy engine.

    Returns:
        Engine: SQLAlchemy engine
    """
    # Use NullPool for development, QueuePool for production
    poolclass = QueuePool if settings.ENVIRONMENT == "production" else NullPool

    engine = create_engine(
        settings.DATABASE_URL,
        echo=settings.DATABASE_ECHO,
        poolclass=poolclass,
        pool_size=settings.DATABASE_POOL_SIZE,
        max_overflow=settings.DATABASE_MAX_OVERFLOW,
        connect_args={"check_same_thread": False}
        if "sqlite" in settings.DATABASE_URL
        else {},
    )
    return engine


engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """Get database session dependency.

    Yields:
        Session: Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
