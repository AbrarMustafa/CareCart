# ------------Project Imports 
from utils.consts import *
from app.response import EmptyDictResponse
from db.database import get_db 
from moduleUser.route import userRouter
from moduleOrder.route import orderRouter
from moduleOrder.enums import OrderStatus
from moduleOrder.model import getTotalOrdersCountModel
from moduleOrder.seed import *


# ------------Lib Imports 
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, status ,Depends
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException

# app = FastAPI(debug=True)
app = FastAPI(
    debug=True,
    # title="CareCart",
    # description="CareCart APIs",
    # version="1.0.0",
    # openapi_url="/api/v1/openapi.json",  # Provide an OpenAPI endpoint
    # docs_url="/docs",  # Set the documentation endpoint
    # redoc_url=None,  # Disable ReDoc (if you don't need it)
    # swagger_ui=True,  # Enable Swagger UI
)


app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
async def catch_exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"details": str(e)}))

app.middleware('http')(catch_exception_middleware)

@app.get("/")
async def root():
    return {"message": "CareCart Apis!"}

# =====================APPS ROUTES====================#
app.include_router(userRouter)
app.include_router(orderRouter)


