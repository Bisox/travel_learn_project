from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.backend.db_depend import get_db
from app.services.help_auth import get_password_hash
from schemas import SUserRegister
from app.services.usersevices import UserService

router = APIRouter(prefix="/auth", tags=["auth&users"])

@router.post("/register")
async def register_user(db: Annotated[AsyncSession, Depends(get_db)], user_data: SUserRegister):
    existing_user = await UserService.find_one_or_none(db, email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(db, email=user_data.email, hashed_password=hashed_password)