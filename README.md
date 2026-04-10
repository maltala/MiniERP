# 📦 MiniERP — Sistema de Gestión Empresarial (FastAPI + SQLite)

MiniERP es una aplicación web ligera diseñada para gestionar productos, clientes y operaciones básicas de un pequeño negocio.  
Está desarrollada con **FastAPI**, **Jinja2**, **SQLAlchemy** y **SQLite**, con una arquitectura limpia y extensible.

---

## 🚀 Características principales

- Gestión completa de productos (CRUD)
- Plantillas HTML con Jinja2
- API documentada automáticamente con Swagger / Redoc
- Base de datos SQLite integrada
- Estructura modular y escalable
- Preparado para Docker (futuro)

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Jinja2**
- **SQLite**
- **HTML + CSS (Bootstrap)**

---

## 📁 Estructura del proyecto

MiniERP/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── templates/
│   └── static/
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ▶️ Cómo ejecutar el proyecto

### 1. Crear entorno virtual

python -m venv venv


### 2. Activarlo (Windows)

venv\Scripts\activate


### 3. Instalar dependencias

pip install -r requirements.txt


### 4. Ejecutar el servidor

uvicorn app.main:app --reload

### 5. Abrir en el navegador

http://127.0.0.1:8000 (127.0.0.1 in Bing)


## 📚 Documentación automática

FastAPI genera documentación interactiva:

- Swagger UI → `/docs`
- Redoc → `/redoc`

---

## 🧩 Próximas mejoras

- Gestión de clientes
- Gestión de pedidos
- Autenticación de usuarios
- Dashboard con estadísticas
- Contenedorización con Docker

---