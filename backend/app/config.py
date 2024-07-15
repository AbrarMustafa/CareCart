# ------------Project Imports 
# ------------Lib Imports 
import os

class Settings():

    PROJECT_NAME:str = "CareCart"
    PROJECT_VERSION: str = "1.0.0"

    # DB_TYPE: str = "POSTGRES"
    # DB_USER : str = "DB_USER"
    # DB_PASSWORD = "DB_PASSWORD"
    # DB_SERVER : str = "localhost"
    # DB_PORT : str = 5432 # default postgres port is 5432
    # DB_NAME : str = "db_name_missing"
    # DATABASE_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    DATABASE_URL = "sqlite:///./test.db"
settings = Settings()
