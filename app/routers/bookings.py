from typing import Annotated

from fastapi import APIRouter, Depends, Request

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.help_auth import get_current_user
from app.backend.db_depend import get_db
from app.services.bookingservice import BookingService
from app.models.users import User
from schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("/")
async def get_bookings(db: Annotated[AsyncSession, Depends(get_db)], user: Annotated[User, Depends(get_current_user)]):
    return await BookingService.find_all(db, user_id=user.id)









