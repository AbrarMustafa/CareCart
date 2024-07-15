# ------------Project Imports 
# ------------Lib Imports 
import os
from pathlib import Path
from dotenv import load_dotenv
from utils.consts import POSTGRES, MYSQL

class Settings():
    load_dotenv(dotenv_path=Path('.') / '.env')

    PROJECT_NAME:str = "CareCart"
    PROJECT_VERSION: str = "1.0.0"

    DB_TYPE: str = POSTGRES
    DB_USER : str = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SERVER : str = os.getenv("DB_SERVER","localhost")
    DB_PORT : str = os.getenv("DB_PORT",5432) # default postgres port is 5432
    DB_NAME : str = os.getenv("DB_NAME","db_name_missing")
    DATABASE_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

settings = Settings()
