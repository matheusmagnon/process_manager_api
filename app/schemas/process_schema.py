from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProcessBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: bool = True

class ProcessCreate(ProcessBase):
    pass

class ProcessUpdate(ProcessBase):
    pass

class ProcessResponse(ProcessBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None  
    
    class Config:
        orm_mode = True
