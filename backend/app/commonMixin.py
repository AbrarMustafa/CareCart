# ------------Project Imports 
from app.config import Settings
from utils.consts import *
from utils.commons import *
 
# ------------Lib Imports 
from sqlalchemy import *
from sqlalchemy.orm import Session, declarative_mixin
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime, date
from typing import Optional, Union, List



# ------------------------------------- DATABASE DATE TIME COLUMN ------------------------------------- #
@declarative_mixin
class DateColumnMixin:
    @declared_attr
    def created_date(cls):
        return Column(DateTime, default= datetime.utcnow)
 