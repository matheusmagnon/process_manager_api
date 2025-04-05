"""
Service layer for handling business logic related to processes.
"""

from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.process_model import Process


class ProcessService:
    """Service class for managing process-related operations."""

    @staticmethod
    async def get_all_processes(db: AsyncSession) -> List[Process]:
        """Retrieve all processes from the database.

        Args:
            db: AsyncSession for database operations.

        Returns:
            List[Process]: List of all processes.
        """
        result = await db.execute(select(Process))
        return result.scalars().all()

    @staticmethod
    async def create_process(db: AsyncSession, process_data: dict) -> Process:
        """Create a new process in the database.

        Args:
            db: AsyncSession for database operations.
            process_data: Dictionary containing process attributes.

        Returns:
            Process: The newly created process.
        """
        new_process = Process(**process_data)
        db.add(new_process)
        await db.commit()
        await db.refresh(new_process)
        return new_process

    @staticmethod
    async def update_process(
        db: AsyncSession, process_id: int, process_data: dict
    ) -> Process:
        """Update an existing process in the database.

        Args:
            db: AsyncSession for database operations.
            process_id: ID of the process to update.
            process_data: Dictionary containing updated process attributes.

        Returns:
            Process: The updated process.
        """
        process = await db.get(Process, process_id)
        if process:
            for key, value in process_data.items():
                setattr(process, key, value)
            await db.commit()
            await db.refresh(process)
        return process

    @staticmethod
    async def delete_process(db: AsyncSession, process_id: int) -> None:
        """Delete a process from the database.

        Args:
            db: AsyncSession for database operations.
            process_id: ID of the process to delete.
        """

        process = await db.get(Process, process_id)
        if process:
            await db.delete(process)
            await db.commit()
