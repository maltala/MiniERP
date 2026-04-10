from sqlalchemy.orm import Session
from app.models.producto_model import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate

def crear_producto(db: Session, data: ProductoCreate):
    producto = Producto(**data)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db, producto_id, data):
    producto = obtener_producto(db, producto_id)
    if not producto:
        return None

    for key, value in data.items():   # ← aquí está el cambio
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto


def eliminar_producto(db: Session, producto_id: int):
    producto = obtener_producto(db, producto_id)
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto

# ✔ CRUD completo
# ✔ Código limpio
# ✔ Preparado para integrarse con API