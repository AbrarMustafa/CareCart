# ------------Project Imports 

from app.config import Settings
from utils.consts import POSTGRES, MYSQL
from app.commonMixin import DateColumnMixin
from db.database import get_db, Base

from moduleUser.request import UserRequest, UserUpdateRequest
from moduleUser.tables import *

# ------------Lib Imports 
from typing import Optional
from sqlalchemy import *
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session, declarative_mixin
from sqlalchemy.ext.declarative import declared_attr
from typing import Dict
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ENUM
# ------------Project Imports 
 
   
# ------------------------------------USER------------------------------------#
# models.py
from sqlalchemy import Column, String, BigInteger, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from main import Base

class UserAccountModel(Base):
    __tablename__ = 'user_accounts'
    id = Column(BigInteger, primary_key=True, nullable=False)
    external_id = Column(String(255), unique=True, nullable=False)
    user_name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_soft_deleted = Column(Boolean, default=False)
    delete_reason = Column(String(255), nullable=True)

class UserLocationModel(Base):
    __tablename__ = 'user_locations'
    id = Column(BigInteger, primary_key=True, nullable=False)
    address = Column(String(255), nullable=True)
    zipcode = Column(String(255), unique=True, nullable=False)
    city = Column(String(255), nullable=True)
    map_address = Column(String(255), nullable=True)

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)
    surname = Column(String(255), nullable=True)
    phone_number = Column(String(255), unique=True, nullable=False)
    account_id = Column(BigInteger, ForeignKey('user_accounts.id', ondelete="RESTRICT"), nullable=False)
    location_id = Column(BigInteger, ForeignKey('user_locations.id', ondelete="RESTRICT"), nullable=False)
    account = relationship("UserAccountModel")
    location = relationship("UserLocationModel")

     

def get_all_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user_request: UserRequest):
    account = UserAccountModel(**user_request.account.dict())
    location = UserLocationModel(**user_request.location.dict())
    db.add(account)
    db.add(location)
    db.commit()
    db.refresh(account)
    db.refresh(location)

    user = UserModel(
        name=user_request.name,
        surname=user_request.surname,
        phone_number=user_request.phone_number,
        account_id=account.id,
        location_id=location.id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
