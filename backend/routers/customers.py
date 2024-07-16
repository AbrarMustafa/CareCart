from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from pydantic import BaseModel, Field
class LoginRequest(BaseModel):
    username: str
    password: str

from fastapi import APIRouter, Depends, HTTPException, status
@router.post("/verify-user/", response_model=schemas.Customer)
def verify_user(login_request: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=login_request.username)
    if user and user.password == login_request.password:
        # Return the user object if login is successful
        customer = crud.get_customer(db, customer_id=user.customer[0].id)
        return customer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

def get_customers(db: Session, from_id: int, limit: int = 100):
    return db.query(models.Customer).filter(models.Customer.id >= from_id).limit(limit).all()

@router.get("/customers/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers
