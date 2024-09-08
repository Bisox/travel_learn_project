from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.backend.db_depend import get_db
from app.models.bookings import Booking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)

@router.get("/")
async def get_bookings(db: Annotated[AsyncSession, Depends(get_db)]):
    query = select(Booking)
    result = await db.execute(query)
    return result.scalars().all()









