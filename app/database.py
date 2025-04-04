"""
Database configuration and session management for SQLAlchemy async operations.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_db():
    """Generator function providing async database sessions.

    Yields:
        AsyncSession: SQLAlchemy async session instance.

    Usage:
        Use as a FastAPI dependency for database operations.
        Automatically handles session cleanup.
    """
    async with AsyncSessionLocal() as session:
        yield session
