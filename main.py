# Relacionamentos Muitos para muitos (N : N)

# Estudantes se inscrevem em cursos.
# Um estudante pode fazer varios cursos
# Um curso pode ter varios estudantes

#Forma simples:
# A relação não precisa guardar dados extras
# Só fazer o relacionamento

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base
#Tabelas curso e aluno

class Aluno(Base):
    __tablename__ = "alunos"

    #Como cria uma coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #Função para imprimir 
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"


class Curso(Base):
    __tablename__ = "cursos"

    #Como cria uma coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #Função para imprimir 
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    

