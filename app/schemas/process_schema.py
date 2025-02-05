"""
Pydantic schemas for Process data modeling and API validation.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProcessBase(BaseModel):
    """Base schema containing common process attributes."""    
    name: str
    description: Optional[str] = None
    status: bool = True

class ProcessCreate(ProcessBase):
    """Schema for creating new processes (request body)."""


class ProcessUpdate(ProcessBase):
    """Schema for updating existing processes (request body)."""


class ProcessResponse(ProcessBase):
    """Schema for process response data (includes database fields)."""

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration for ORM compatibility."""
        orm_mode = True
        