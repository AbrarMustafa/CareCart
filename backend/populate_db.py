import json
import os
import sys
from datetime import datetime

# Get the absolute path to the current directory
current_dir = os.path.dirname(__file__)
# Construct the absolute path to the data directory
data_dir = os.path.join(current_dir, 'data')

# Add the data directory to the sys.path
sys.path.append(data_dir)

from database import SessionLocal, engine
import models, schemas, crud

def load_data():
    db = SessionLocal()
    with open(os.path.join(data_dir, 'orders.json')) as f:
        orders_data = json.load(f)
        for order in orders_data['Orders']:
            # Convert created_date and product_delivery_date to datetime objects
            order['created_date'] = datetime.strptime(order['created_date'], '%Y-%m-%d')
            order['product_delivery_date'] = datetime.strptime(order['product_delivery_date'], '%Y-%m-%d')
            db_order = schemas.OrderCreate(**order)
            crud.create_order(db, db_order)
    
    with open(os.path.join(data_dir, 'customers.json')) as f:
        customers_data = json.load(f)
        for customer in customers_data['Customers']:
            # Convert created to datetime object
            customer['account']['created'] = datetime.fromtimestamp(customer['account']['created'])
            account_data = customer.pop('account')
            location_data = customer.pop('location')
            # Convert created to datetime object for location
            location_data['created'] = datetime.fromtimestamp(location_data['created'])
            db_account = models.Account(**account_data)
            db_location = models.Location(**location_data)
            db.add(db_account)
            db.add(db_location)
            db.commit()
            db.refresh(db_account)
            db.refresh(db_location)
            customer['account_id'] = db_account.id
            customer['location_id'] = db_location.id
            db_customer = schemas.CustomerCreate(**customer)
            crud.create_customer(db, db_customer)
    db.close()
if __name__ == "__main__":
    load_data()
