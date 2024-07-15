# ------------Project Imports 

# ------------Lib Imports 
from pydantic import BaseModel,validator
from pydantic.types import conint
from decimal import Decimal
from typing import Optional


class UserAccountRequest(BaseModel):
    external_id: str
    user_name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    is_verified: Optional[bool] = False
    is_active: Optional[bool] = True
    is_soft_deleted: Optional[bool] = False
    delete_reason: Optional[str] = None

class UserLocationRequest(BaseModel):
    address: Optional[str] = None
    zipcode: str
    city: Optional[str] = None
    map_address: Optional[str] = None

class UserRequest(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone_number: str
    account: UserAccountRequest
    location: UserLocationRequest