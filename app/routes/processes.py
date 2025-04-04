"""
API routes for managing processes.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.process_service import ProcessService
from app.schemas.process_schema import ProcessCreate, ProcessUpdate, ProcessResponse
from app.models.process_model import Process
from app.database import get_db

router = APIRouter(prefix="/processes", tags=["Processes"])


@router.post("/", response_model=ProcessResponse, status_code=status.HTTP_201_CREATED)
async def create_process(
    process_data: ProcessCreate, db: AsyncSession = Depends(get_db)
):
    """Create a new process.

    Args:
        process_data: Data for the new process.
        db: Database session.

    Returns:
        ProcessResponse: The created process.
    """
    return await ProcessService.create_process(db, process_data.dict())


@router.get("/", response_model=list[ProcessResponse])
async def get_all_processes(db: AsyncSession = Depends(get_db)):
    """Retrieve all processes.

    Args:
        db: Database session.

    Returns:
        list[ProcessResponse]: List of all processes.
    """
    return await ProcessService.get_all_processes(db)


@router.get("/{process_id}", response_model=ProcessResponse)
async def get_process(process_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve a specific process by ID.

    Args:
        process_id: ID of the process to retrieve.
        db: Database session.

    Raises:
        HTTPException: If the process is not found.

    Returns:
        ProcessResponse: The requested process.
    """
    process = await db.get(Process, process_id)
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return process


@router.put("/{process_id}", response_model=ProcessResponse)
async def update_process(
    process_id: int, process_data: ProcessUpdate, db: AsyncSession = Depends(get_db)
):
    """Update an existing process.

    Args:
        process_id: ID of the process to update.
        process_data: Updated data for the process.
        db: Database session.

    Raises:
        HTTPException: If the process is not found.

    Returns:
        ProcessResponse: The updated process.
    """
    process = await ProcessService.update_process(
        db, process_id, process_data.dict(exclude_unset=True)
    )
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return process


@router.delete("/{process_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_process(process_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a process by ID.

    Args:
        process_id: ID of the process to delete.
        db: Database session.
    """
    await ProcessService.delete_process(db, process_id)
