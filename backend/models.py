from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    contact_number = Column(String)
    note = Column(String, nullable=True)
    created_date = Column(DateTime)
    product_delivery_date = Column(DateTime)
    shopper_id = Column(Integer, ForeignKey('customers.id'))
    cart_id = Column(Integer)
    user_account_id = Column(Integer, ForeignKey('accounts.id'))
    tip = Column(Float)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    user_account = relationship("Account", back_populates="orders")

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime, nullable=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))

    # Relationships
    account = relationship("Account", back_populates="customer")
    location = relationship("Location", back_populates="customer")
    orders = relationship("Order", back_populates="customer")

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String)
    user_name = Column(String)
    password = Column(String)
    email = Column(String)
    is_verified = Column(Boolean)
    is_active = Column(Boolean)
    is_soft_deleted = Column(Boolean)
    delete_reason = Column(String, nullable=True)
    created = Column(DateTime)
    edited = Column(DateTime, nullable=True)

    # Relationships
    customer = relationship("Customer", back_populates="account")
    orders = relationship("Order", back_populates="user_account")

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    zipcode = Column(String)
    city = Column(String)
    map_address = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime, nullable=True)

    # Relationships
    customer = relationship("Customer", back_populates="location")
