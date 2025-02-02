from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.process_model import Process

class ProcessService:
    @staticmethod
    async def get_all_processes(db: AsyncSession) -> List[Process]:
        result = await db.execute(select(Process))
        return result.scalars().all()

    @staticmethod
    async def create_process(db: AsyncSession, process_data: dict) -> Process:
        new_process = Process(**process_data)
        db.add(new_process)
        await db.commit()
        await db.refresh(new_process)
        return new_process

    @staticmethod
    async def update_process(db: AsyncSession, process_id: int, process_data: dict) -> Process:
        process = await db.get(Process, process_id)
        if process:
            for key, value in process_data.items():
                setattr(process, key, value)
            await db.commit()
            await db.refresh(process)
        return process

    @staticmethod
    async def delete_process(db: AsyncSession, process_id: int) -> None:
        process = await db.get(Process, process_id)
        if process:
            await db.delete(process)
            await db.commit()