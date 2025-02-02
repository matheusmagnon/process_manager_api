from fastapi import APIRouter, Depends, HTTPException, status
from app.services.process_service import ProcessService
from app.schemas.process_schema import ProcessCreate, ProcessUpdate, ProcessResponse
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/processes", tags=["Processes"])

@router.post("/", response_model=ProcessResponse, status_code=status.HTTP_201_CREATED)
async def create_process(
    process_data: ProcessCreate,
    db: AsyncSession = Depends(get_db)
):
    return await ProcessService.create_process(db, process_data.dict())

@router.get("/", response_model=list[ProcessResponse])
async def get_all_processes(db: AsyncSession = Depends(get_db)):
    return await ProcessService.get_all_processes(db)

@router.get("/{process_id}", response_model=ProcessResponse)
async def get_process(process_id: int, db: AsyncSession = Depends(get_db)):
    process = await db.get(Process, process_id)
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return process

@router.put("/{process_id}", response_model=ProcessResponse)
async def update_process(
    process_id: int,
    process_data: ProcessUpdate,
    db: AsyncSession = Depends(get_db)
):
    process = await ProcessService.update_process(db, process_id, process_data.dict(exclude_unset=True))
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return process

@router.delete("/{process_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_process(process_id: int, db: AsyncSession = Depends(get_db)):
    await ProcessService.delete_process(db, process_id)