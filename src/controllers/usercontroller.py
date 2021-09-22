import asyncio

from src.database.configuration import session
from src.database.schemas import User

# Função que permite criar usuários
async def create_user(user: User):
  # Abrindo uma sessão no banco
  async with session() as s:
    s.add( user ) # Criando uma solicitação de adição
    await s.commit() # Aceitando a solicitação e criando o usuário no banco de dados
    await s.refresh( user )

    return user.id