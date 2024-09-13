from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db_depend import get_db
from app.services.bookingservice import BookingService
from schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)

@router.get("/", response_model=list[SBooking])
async def get_bookings(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await BookingService.find_all(db)
    return result









