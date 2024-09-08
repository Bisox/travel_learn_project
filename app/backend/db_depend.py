from sqlalchemy.ext.asyncio import AsyncSession
from app.backend.database import async_session_maker


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            print(f"Ошибка при работе с сессией БД: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()
