import asyncio

from src.database.configuration import engine
from src.database.schemas import Base

# Função que permite criar o banco de dados após iniciar a engine
async def create_database():
  # Estabelecendo uma conexão com a engine
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)
    await conn.run_sync(Base.metadata.create_all)

# asyncio.run( create_database() )