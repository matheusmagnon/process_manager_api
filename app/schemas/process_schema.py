from datetime import datetime
from pydantic import BaseModel

class ProcessBase(BaseModel):
    name: str
    description: str | None = None
    status: bool = True

class ProcessCreate(ProcessBase):
    pass

class ProcessUpdate(ProcessBase):
    pass

class ProcessResponse(ProcessBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True