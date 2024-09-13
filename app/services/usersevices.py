from app.models.users import User
from app.services.basesevice import BaseService



class UserService(BaseService):
    model = User


