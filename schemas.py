from datetime import date

from pydantic import BaseModel, EmailStr


class SBooking(BaseModel):

    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: float
    total_cost: float
    total_days: int

    class Config:
        from_attributes = True


class SUserRegister(BaseModel):
    email: EmailStr
    password: str

