from beanie import init_beanie
from fastapi import FastAPI
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from src.config import MONGO_DB, MONGO_URI
from src.middlewares import NginxHeadersMiddleware
from src.models.db import DialogModel, DomainModel
from src.router import router as api_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(NginxHeadersMiddleware)
app.include_router(api_router, prefix="/api", tags=["api"])


@app.on_event("startup")
async def startup() -> None:
    logger.info("Connecting to MongoDB")
    logger.info(MONGO_URI)

    await init_beanie(
        database=AsyncIOMotorClient(MONGO_URI)[MONGO_DB],
        document_models=[DialogModel, DomainModel],
    )
