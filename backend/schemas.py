from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class OrderBase(BaseModel):
    address: str
    contact_number: str
    note: Optional[str] = None
    created_date: datetime = Field(..., alias='created_date', description='Order creation date')
    product_delivery_date: datetime = Field(..., alias='product_delivery_date', description='Product delivery date')
    shopper_id: int
    cart_id: int
    user_account_id: int
    tip: float

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d')
        }

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

class AccountBase(BaseModel):
    external_id: str
    user_name: str
    password: str
    email: str
    is_verified: bool
    is_active: bool
    is_soft_deleted: bool
    delete_reason: Optional[str] = None
    created: datetime
    edited: Optional[datetime] = None

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    address: str
    zipcode: str
    city: str
    map_address: str
    created: datetime
    edited: Optional[datetime] = None

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str
    surname: str
    phone_number: str
    created: datetime
    edited: Optional[datetime] = None
    account_id: int
    location_id: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
