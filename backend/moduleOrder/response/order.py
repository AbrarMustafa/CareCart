# ------------Project Imports 
from app.response import BaseResponse, CreatedUpdatedResponse

# ------------Lib Imports 
from pydantic import BaseModel, Json
from pydantic.types import conint
from datetime import datetime
from decimal import Decimal
from typing import Optional


# ------------------------------------ORDER------------------------------------#
class OrderModelResponse(CreatedUpdatedResponse, BaseModel):
    id: Optional[int] = 0
    user_account_id: Optional[int] = 0
    shopper_id: Optional[int] = 0
    cart_id: Optional[int] = 0
    address: Optional[str] = ""
    contact_number: Optional[str] = ""
    note: Optional[str] = ""
    tip: Optional[int] = 0
    created_date: Optional[str] = None


class OrdersResponse(BaseResponse):
    data: Optional[list[OrderModelResponse]]
    
