# ------------Project Imports 

from app.commonMixin import DateColumnMixin
from db.database import get_db, Base
 
from moduleUser.tables import *
from moduleOrder.tables import *
from moduleOrder.request import OrderRequest

# ------------Lib Imports 
import json
from datetime import datetime, date
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqlalchemy import *
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session, declarative_mixin
from sqlalchemy.ext.declarative import declared_attr
from typing import Dict
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ENUM


# ------------------------------------ORDER------------------------------------#
class OrderModel(DateColumnMixin, Base):
    __tablename__ = OrderTable
    id = Column(BigInteger, primary_key=True,  nullable=False)
    user_account_id = Column(BigInteger, ForeignKey(UserTable+".id",  ondelete="RESTRICT"), nullable=False)
    shopper_id = Column(BigInteger,  nullable=True)
    cart_id = Column(BigInteger,  nullable=True)
    address = Column(String(255), nullable=True)
    contact_number = Column(String(255), nullable=True)
    note = Column(String(255), nullable=True)
    tip = Column(BigInteger,  nullable=True)
    product_delivery_date = Column(DateTime, default= datetime.utcnow)

    def __str__(self): # This will get called when print(str(AttributeTypesModel(id=1)))
        return f"{self.id}"

def getUserOrdersModel(db: Session, user):
    orders = db.query(OrderModel)
    orders= orders.filter(OrderModel.user_id==user.id)
    return orders


def createOrderModel(db: Session, orderRequest: OrderRequest, user):
    # ---------------------------------------- PLACING ORDER ---------------------------------------- #
    order = OrderModel(user_account_id = orderRequest.user_account_id, shopper_id = orderRequest.shopper_id, 
                    user_id = user.id, cart_id = orderRequest.cart_id, address = orderRequest.address, 
                    contact_number = orderRequest.contact_number, note = orderRequest.note, tip = orderRequest.tip, product_delivery_date = orderRequest.product_delivery_date,)
    db.add(order)
    db.commit()
    db.refresh(order)

    return order
