# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
from books_route import router as books_router

app = FastAPI()

app.include_router(books_router)

@app.get("/")
async def read_main():
    return {"message": "Hello Bigger Applicationss!"}