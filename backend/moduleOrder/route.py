# ------------Project Imports 
from utils.consts import *
from moduleOrder.model import *
from moduleOrder.depends import * 
from moduleOrder.request import OrderRequest
from moduleOrder.wrapper import createOrder, getOrders

# ------------Lib Imports 
from fastapi import *
from sqlalchemy.orm import Session
from db.database import get_db 


orderRouter = APIRouter(prefix='/order', tags = ['OrderApi'])

# ------------------------------------ORDER------------------------------------#

@orderRouter.get('', status_code= status.HTTP_201_CREATED )
async def getOrdersApi(request: Request, db: Session = Depends(get_db)): 
    return getOrders(db = db, user= request.state.user)


@orderRouter.post('', status_code= status.HTTP_201_CREATED) 
async def createOrderApi(request: Request, orderRequest: OrderRequest, db: Session = Depends(get_db)): 
    return createOrder(db = db, orderRequest = orderRequest, user= request.state.user)
 
