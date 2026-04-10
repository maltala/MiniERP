# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MiniERP"
    DATABASE_URL: str = "sqlite:///./minierp.db"

    class Config:
        env_file = ".env"

settings = Settings()

 #Ahora sí compatible con Pydantic 2
 #No rompe nada del resto del proyecto
 #FastAPI lo aceptará sin problemas
