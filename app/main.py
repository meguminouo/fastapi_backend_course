from fastapi import FastAPI ,Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine ,Column ,Integer ,String ,Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,Session

from .database import Base, engine
from .routers import router

app = FastAPI()

# Initialize Database's Table
Base.metadata.create_all(bind=engine) 

# Register Router
app.include_router(router=router, prefix="/api", tegs=["todos"])