from fastapi import FastAPI
from app.routers import bookings, users

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(users.router)
app.include_router(bookings.router)



