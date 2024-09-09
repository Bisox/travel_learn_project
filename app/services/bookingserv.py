from typing import Annotated

from fastapi import Depends

from sqlalchemy import select

from app.models.bookings import Booking


class BookingService:

    @classmethod
    async def find_all(cls, db):
        query = select(Booking)
        bookings = await db.execute(query)
        return bookings.mappings().all()