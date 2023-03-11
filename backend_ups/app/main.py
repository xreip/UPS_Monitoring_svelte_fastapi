from fastapi import FastAPI, Body, Cookie, Depends, Header, Query, Path
from pydantic import BaseModel, Field, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

# from app.api.api import api_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ups")
def get_ups():
    return [
        {
            "name": "UPS Dell Phase 1",
            "model": "Dell 1920W Power",
            "status": "online",
            "batt_charge": 100,
            "load": 45,
            "voltage": 26.3,
        },
        {
            "name": "UPS Dell Phase 2",
            "model": "Dell 1920W Power",
            "status": "onbatt",
            "batt_charge": 64,
            "load": 12,
            "voltage": 25.6,
        },
        {
            "name": "UPS Eaton Main Server",
            "model": "Eaton 800W v2.0",
            "status": "lowbatt",
            "batt_charge": 24,
            "load": 25,
            "voltage": 24.9,
        },
        {
            "name": "UPS Dell SimFarm",
            "model": "Dell Tower 2000W Power",
            "status": "disconnected",
            "batt_charge": 0,
            "load": 0,
            "voltage": 0,
        },
    ]
