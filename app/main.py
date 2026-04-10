# app/main.py
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from app.api.v1.productos import router as productos_router
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.services.productos_service import (
    obtener_productos,
    crear_producto,
    obtener_producto,
    actualizar_producto,
    eliminar_producto
)

# Inicializar aplicación
app = FastAPI(title="MiniERP", version="0.1.0")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir routers de API
app.include_router(productos_router, prefix="/productos", tags=["Productos"])

# Configurar plantillas Jinja2
templates = Jinja2Templates(directory="app/templates")

# 🟩 LISTAR PRODUCTOS
@app.get("/productos/listar")
def listar_productos(request: Request):
    db = SessionLocal()
    try:
        productos = obtener_productos(db) or []
        print("DEBUG tipo:", type(productos))
        print("DEBUG contenido:", productos)
    except Exception as e:
        print("Error al obtener productos:", e)
        productos = []
    finally:
        db.close()

    return templates.TemplateResponse(
        name="productos_listar.html",
        context={"request": request, "productos": productos},
        request=request
    )


# 🟦 CREAR PRODUCTO
@app.get("/productos/nuevo")
def nuevo_producto_form(request: Request):
    return templates.TemplateResponse(
        name="productos_nuevo.html",
        context={"request": request},
        request=request
    )


@app.post("/productos/nuevo")
def nuevo_producto_submit(request: Request, nombre: str = Form(...), precio: float = Form(...), stock: int = Form(...)):
    db = SessionLocal()
    data = {"nombre": nombre, "precio": precio, "stock": stock}
    crear_producto(db, data)
    db.close()

    return RedirectResponse(
        url="/productos/listar",
        status_code=303
    )


# 🟧 EDITAR PRODUCTO
@app.get("/productos/editar/{producto_id}")
def editar_producto_form(request: Request, producto_id: int):
    db = SessionLocal()
    producto = obtener_producto(db, producto_id)
    db.close()

    return templates.TemplateResponse(
        name="productos_editar.html",
        context={"request": request, "producto": producto},
        request=request
    )

from fastapi import Form  # asegúrate de tener este import arriba

@app.post("/productos/actualizar/{producto_id}")
def actualizar_producto_submit(
    request: Request,
    producto_id: int,
    nombre: str = Form(...),
    precio: float = Form(...),
    stock: int = Form(...)
):
    db = SessionLocal()
    data = {"nombre": nombre, "precio": precio, "stock": stock}

    actualizar_producto(db, producto_id, data)
    productos = obtener_productos(db)
    db.close()

    return RedirectResponse(
        url="/productos/listar",
        status_code=303
    )


@app.post("/productos/editar/{producto_id}")
def editar_producto_submit(
    request: Request,
    producto_id: int,
    nombre: str = Form(...),
    precio: float = Form(...),
    stock: int = Form(...)
):
    db = SessionLocal()
    actualizar_producto(db, producto_id, {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    productos = obtener_productos(db)
    return templates.TemplateResponse(
        "productos_listar.html",
        {"request": request, "productos": productos}
    )

# 🟥 ELIMINAR PRODUCTO
@app.get("/productos/eliminar/{producto_id}")
def eliminar_producto_confirm(request: Request, producto_id: int):
    db = SessionLocal()
    producto = obtener_producto(db, producto_id)
    db.close()

    return templates.TemplateResponse(
        name="productos_eliminar.html",
        context={"request": request, "producto": producto},
        request=request
)


@app.post("/productos/eliminar/{producto_id}")
def eliminar_producto_submit(request: Request, producto_id: int):
    db = SessionLocal()
    eliminar_producto(db, producto_id)
    productos = obtener_productos(db)
    db.close()

    return RedirectResponse(
        url="/productos/listar",
        status_code=303
    )


from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="app/static"), name="static")
