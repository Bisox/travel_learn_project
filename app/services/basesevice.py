from sqlalchemy import select, insert


class BaseService:

    model = None

    @classmethod
    async def find_by_id(cls, db, model_id):
        query = select(cls.model).filter_by(id=model_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, db, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, db, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await db.execute(query)
        return result.scalars().all()

    @classmethod
    async def add(cls, db, **data):
        query = insert(cls.model).values(**data)
        await db.execute(query)
        await db.commit()