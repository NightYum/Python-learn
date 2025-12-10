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

for book in books:
    if book["id"] == 1:
        print(book)
    else:
        print("book not found")