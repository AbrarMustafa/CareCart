# ------------Project Imports 

# ------------Lib Imports 
from pydantic import BaseModel,validator
from pydantic.types import conint
from datetime import datetime
from decimal import Decimal
from typing import Optional

class OrderRequest(BaseModel):
    user_account_id :Optional[int] =0
    shopper_id :Optional[int] =0
    cart_id :Optional[int] =0
    address :Optional[str] = None
    contact_number :Optional[str] = None
    note :Optional[str] = None
    tip :Optional[int] = 0
    product_delivery_date :Optional[str] = None
