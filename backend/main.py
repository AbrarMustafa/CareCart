from fastapi import FastAPI
from routers import orders, customers
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

# app = FastAPI(debug=True)
app = FastAPI(
    debug=True,
    title="BuyCom",
    description="BuyCom APIs",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",  # Provide an OpenAPI endpoint
    docs_url="/docs",  # Set the documentation endpoint
    redoc_url=None,  # Disable ReDoc (if you don't need it)
    swagger_ui=True,  # Enable Swagger UI
)

app.include_router(orders.router)
app.include_router(customers.router)

# GraphQL endpoint can be added as well if needed.
