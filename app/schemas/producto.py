from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int = 0

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True


# ✔ ProductoCreate para crear
# ✔ ProductoUpdate para modificar
# ✔ ProductoOut para devolver datos
# ✔ Compatible con Pydantic v2