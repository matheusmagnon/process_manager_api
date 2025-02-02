from fastapi import FastAPI
from app.routes.processes import router as process_router
from app.database import engine, Base
from app.config import settings
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Process Manager API", debug=settings.debug)

instrumentator = Instrumentator()

instrumentator.instrument(app).expose(app, include_in_schema=False)

# Configuração CORS (se necessário)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # Criar tabelas se não existirem
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(process_router)