# ------------Project Imports 

from app.response import BaseResponse, CreatedUpdatedResponse
from moduleUser.model import *
from moduleUser.request import *

# ------------Lib Imports 

from pydantic import BaseModel,validator
from pydantic.types import conint
from decimal import Decimal
from typing import Optional



# ------------------------------------OTP------------------------------------#
# class OtpResponse(BaseResponse):
#     data: Optional[EmptyResponse]
  
# ------------------------------------USER------------------------------------#
class UserResponse(CreatedUpdatedResponse, BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    phone_number: str
    account: UserAccountRequest
    location: UserLocationRequest

    class Config:
        orm_mode = True


class UsersResponse(BaseResponse):
    data: Optional[list[UserResponse]]
    
class UserResponse(BaseResponse):
    data: Optional[UserResponse]
   