from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.reviews.models import Review



engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

async def initdb():
    """Create init database model in the database"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

