"""
Main FastAPI application module with configurations and routes setup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator


from app.routes.processes import router as process_router
from app.database import engine, Base
from app.config import settings

app = FastAPI(title="Process Manager API", debug=settings.debug)


instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app, include_in_schema=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    """Initialize application services on startup.
    
    Creates database tables if they don't exist.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(process_router)
