# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    sexo = Column(String(1), nullable=False)
    
class Pessoa2(Base):
    __tablename__ = 'pessoa2'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String(1), nullable=False)

class Notas(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True)
    nome_aluno = Column(String(50), nullable=False)
    email_aluno = Column(String(50), nullable=False)
    nota = Column(Integer, nullable=False)
