from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

# ✔ Modelo simple
# ✔ Realista
# ✔ Compatible con SQLite y PostgreSQL
# ✔ Preparado para CRUD