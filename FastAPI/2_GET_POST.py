import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Programming",
        "author": "Me",
    },
    {
        "id": 2,
        "title": "Python Programmings",
        "author": "Me",
    }
]

@app.get(
    "/",
    summary="Главная ручка",
    tags=["Ручки"])
def read_books():
    return "Main Page"

@app.get(
    "/books",
    summary="Получить все книги",
    tags=["Книги"])
def read_books():
    return books

@app.get(
    "/books/{book_id}",
    summary="Получить конкретную книгу",
    tags=["Книги"])
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewBook(BaseModel):
    title: str
    author: str

@app.post(
    "/books",
    summary="Добавить книгу",
    tags=["Книги"]
)
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Книга успешно добавлена"}

if __name__ == "__main__":
    uvicorn.run("2:app", host="127.0.0.1", port=8000, reload=True)

# 3 способа запустить fastapi
# pip install "fastapi[standard], далее в командной строке fastapi dev main.py
# uvicorn main:app --reload
# Через if name = main, в командной строке python main.py