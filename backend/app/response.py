# ------------Project Imports 
from app.commonMixin import *
from utils.consts import *

# ------------Lib Imports 
from pydantic import BaseModel, validator
from typing import Optional, Union
from datetime import date
import re

class BaseResponse(BaseModel):
    # success , msg = True, "" 
    success: bool = True
    msg: str = ""
    
class EmptyDictResponse(BaseResponse):
    data: dict
class EmptyListResponse(BaseResponse):
    data: list


class CreatedUpdatedResponse(BaseModel):
    created_at: Union[date, str]
    updated_at: Union[date, str]
    
    @validator("created_at", pre=True, always=True)
    def parse_created_at_date(cls, value):
        return parseDBDateTime(value)
    
    @validator("updated_at", pre=True, always=True)
    def parse_updated_at_date(cls, value):
        return parseDBDateTime(value)
    