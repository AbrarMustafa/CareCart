# ------------Project Imports 
from moduleUser.model import *
from app.response import EmptyDictResponse
from moduleUser.request import UserRequest
from moduleUser.response import  UserResponse

# ------------Lib Imports 
from fastapi import *
from sqlalchemy.orm import Session
from db.database import get_db 

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from mails.email import send_email
from typing import List

userRouter = APIRouter(prefix='/user', tags = ['UserApi'])


@userRouter.get("/users", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users

@userRouter.post("/user", response_model=UserResponse)
def create_new_user(user: UserRequest, db: Session = Depends(get_db)):
    return create_user(db, user)