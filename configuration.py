from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho onde o banco de dados deve ficar
DATABASE_URL = 'sqlite+aiosqlite:///example.db'

# Criando a engine que faz comunicação com o banco
engine = create_async_engine(DATABASE_URL)

# Criando a sessão
session = sessionmaker(future=True, class_=AsyncSession, bind=engine)

Base = declarative_base()