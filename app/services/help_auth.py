from datetime import datetime, timedelta
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request, HTTPException, Depends, status
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import EmailStr

from config import settings
from app.services.usersevices import UserService
from app.backend.db_depend import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(db, email: EmailStr, password: str):
    user = await UserService.find_one_or_none(db, email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=401, detail='Token is missing')
    return token


async def get_current_user(db: Annotated[AsyncSession, Depends(get_db)], token: Annotated[str, Depends(get_token)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid')
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is expired')
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User does not exist')
    user = await UserService.find_by_id(db, model_id=int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User does not exist')
    return user

