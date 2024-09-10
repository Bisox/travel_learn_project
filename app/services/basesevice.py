from sqlalchemy import select


class BaseService:

    model = None

    @classmethod
    async def find_all(cls, db):
        query = select(cls.model)
        result = await db.execute(query)
        return result.mappings().all()