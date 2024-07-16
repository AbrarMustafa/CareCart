from fastapi import FastAPI
from routers import orders, customers
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


app.include_router(orders.router)
app.include_router(customers.router)

# GraphQL endpoint can be added as well if needed.
