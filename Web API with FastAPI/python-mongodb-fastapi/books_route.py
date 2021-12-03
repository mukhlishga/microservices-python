from fastapi import APIRouter
from books_api import *

router = APIRouter()

@router.post("/bookbyid")
async def view_search_books_id(params:dict):
    result = search_books_id(**params)
    return result
  
@router.post("/bookbyname")
async def view_search_books_by_name(params:dict):
    result = search_book_by_name(**params)
    return result

@router.post("/books")
async def view_search_books_by_name():
    result = search_books()
    return result