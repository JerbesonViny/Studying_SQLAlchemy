from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False, unique=True)
  password = Column(Text, nullable=False)

  def __repr__(self) -> str:
    return f"<User(Name={self.name}, Email={self.email})>"
