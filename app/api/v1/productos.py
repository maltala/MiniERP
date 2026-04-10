from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoOut
from app.services import productos_service

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoOut)
def crear(data: ProductoCreate, db: Session = Depends(get_db)):
    return productos_service.crear_producto(db, data)

@router.get("/", response_model=list[ProductoOut])
def listar(db: Session = Depends(get_db)):
    return productos_service.obtener_productos(db)

@router.get("/{producto_id}", response_model=ProductoOut)
def obtener(producto_id: int, db: Session = Depends(get_db)):
    producto = productos_service.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=ProductoOut)
def actualizar(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    producto = productos_service.actualizar_producto(db, producto_id, data)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/{producto_id}")
def eliminar(producto_id: int, db: Session = Depends(get_db)):
    producto = productos_service.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}

# ✔ API REST completa
# ✔ Validación automática
# ✔ Errores bien gestionados