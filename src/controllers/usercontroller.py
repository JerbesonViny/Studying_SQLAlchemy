from sqlalchemy.future import select
import asyncio

from src.database.configuration import session
from src.database.schemas import User

# Função que permite criar usuários
async def create_user(user: User) -> int:
  # Abrindo uma sessão no banco
  async with session() as s:
    s.add( user ) # Criando uma solicitação de adição
    await s.commit() # Aceitando a solicitação e criando o usuário no banco de dados
    await s.refresh( user )

    return user.id

# Funçao de listar todos os usuários existentes
async def list_users() -> list:
  # Abrindo uma sessão no banco
  async with session() as s:
    query = await s.execute(
      select(User)
    ) # Executando a consulta na tabela de usuários

    # Retornando todos os usuários que foram obtidos a partir da query
    return query.scalars().all()
