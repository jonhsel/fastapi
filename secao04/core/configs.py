from pydantic import BaseSettings
from sqlalchemy.ext.declarative import delcarative_base


class Settings(BaseSettings):
    """
        Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = "api/v1"
    DB__URL: str = "postgresql+asyncpg://geek:university@localhost:5432/faculdade"
    DBBaseModel = delcarative_base()

    class Config:
        case_sensitive = True

settings = Settings()