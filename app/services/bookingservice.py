from app.models.bookings import Booking
from app.services.basesevice import BaseService


class BookingService(BaseService):
    model = Booking

