from fastapi import (
    FastAPI,
    Body,
    Cookie,
    Depends,
    Header,
    Query,
    Path,
    HTTPException,
    status,
)

from pydantic import BaseModel, Field, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

# OTP
import pyotp
import time

# from app.api.api import api_router

app = FastAPI()

origins = [
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
    return {"This": "works"}


class UpsModel(BaseModel):
    name: str
    model: str
    status: str
    batt_charge: int
    load: int
    voltage: float


@app.get("/ups", response_model=list[UpsModel])
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


# AUTH OTP
class OtpSubmit(BaseModel):
    code: str = Field(
        ..., example="123456", max_length=6, min_length=6, description="The OTP code"
    )


class OtpResponse(BaseModel):
    code: str
    good: bool


@app.get("/otp")
def get_otp():
    totp = pyotp.TOTP("JNVZOEU")
    code = totp.now()
    return {"OTP": code}


@app.post("/otp", response_model=OtpResponse)
def verify_otp(OtpSubmit: OtpSubmit):
    code = OtpSubmit.code
    totp = pyotp.TOTP("JNVZOEU")
    isOk = totp.verify(code)
    if not isOk:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unauthorized",
        )
    return {"code": code, "good": isOk}
