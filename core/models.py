from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Tabla para la relación M:N entre juegos y consolas
juegos_consolas = Table(
    "juegos_consolas",
    Base.metadata,
    Column("juego_id", ForeignKey("juegos.id"), primary_key=True),
    Column("consola_id", ForeignKey("consolas.id"), primary_key=True),
)

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    sede_central = Column(String(100))

    consolas = relationship("Consola", back_populates="empresa")

class Consola(Base):
    __tablename__ = "consolas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2))
    fecha_lanzamiento = Column(Date)
    empresa_id = Column(ForeignKey("empresas.id"))  # apunta correctamente a empresas

    empresa = relationship("Empresa", back_populates="consolas")
    juegos = relationship(
        "Juego",
        secondary=juegos_consolas,
        back_populates="consolas"
    )

class Juego(Base):
    __tablename__ = "juegos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

    consolas = relationship(
        "Consola",
        secondary=juegos_consolas,
        back_populates="juegos"
    )