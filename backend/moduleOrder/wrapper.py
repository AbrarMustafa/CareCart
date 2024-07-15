# ------------Project Imports 
from utils.consts import *
from moduleOrder.model import *
from moduleOrder.request import OrderRequest
from moduleOrder.response.order import OrderModelResponse
from moduleOrder.helper import viewCartHelper
from moduleOrder.response.order import *

# ------------Lib Imports 
import json
from fastapi import *
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


# ------------------------------------CART------------------------------------#

def getOrders(db: Session, user):
    _success, _msg, _data = False, SOMETHING_WENT_WRONG, []
    try:
        _data = getUserOrdersModel(db=db, user= user)
        _success, _msg= True, SUCCESS
    except Exception as msg:
       _success, _msg, _data= False, str(msg), []
    response = PaginateOrdersResponse(success = _success, msg = _msg, data = OrderWithTotalResponse( orders=[jsonable_encoder(item) for item in _data ]))  
    return response


def createOrder(db: Session, orderRequest: OrderRequest, user):
    _success, _msg, _data = False, SOMETHING_WENT_WRONG, None
    try:
        _data = createOrderModel(db=db, orderRequest=orderRequest, user= user)
        _success, _msg= True, SUCCESS
    except Exception as msg:
       _success, _msg, _data= False, str(msg), None
    response = OrderResponse(success = _success, msg = _msg, data = jsonable_encoder(_data))  
    return response

