"""
Database model definition for the Process entity.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from app.database import Base


class Process(Base):
    """SQLAlchemy model representing a process in the database.

    Attributes:
        id: Primary key and unique identifier for the process.
        name: Name of the process (max 100 characters).
        description: Optional description of the process (max 500 characters).
        status: Boolean flag indicating if the process is active (default True).
        created_at: Timestamp of when the process was created.
        updated_at: Timestamp of the last update to the process.
    """

    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now)
