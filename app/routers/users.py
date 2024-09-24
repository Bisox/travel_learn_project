from os import access

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated



from app.backend.db_depend import get_db
from app.services.help_auth import get_password_hash, authenticate_user
from app.services.help_auth import verify_password, create_access_token
from schemas import SUserAuth
from app.services.usersevices import UserService

router = APIRouter(prefix="/auth", tags=["auth&users"])

@router.post("/register")
async def register_user(db: Annotated[AsyncSession, Depends(get_db)], user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(db, email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(db, email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def register_user(db: Annotated[AsyncSession, Depends(get_db)], response: Response, user_data: SUserAuth):
    user = await authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token({'sub': user.id})
    response.set_cookie(key='booking_access_token', value=access_token, httponly=True)
    return {'access_token': access_token}

