from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    serverid = Column(String(18), nullable=False)
    userid = Column(String(18), nullable=False)
    basados = Column(Integer, default=0)
    ultimobasado = Column(Float, default=0)

    def __repr__(self) -> str:
        return f"User(serverid={self.serverid}, userid={self.userid}, basados={self.basados}, ultimobasado={self.ultimobasado})"

sessionClass = sessionmaker(engine)
session = sessionClass()