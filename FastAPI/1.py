import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Главная ручка", tags=["Ручки"])
def root():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("1:app", host="0.0.0.0", port=8000, reload=True)

# 3 способа запустить fastapi
# pip install "fastapi[standard], далее в командной строке fastapi dev 1.py
# uvicorn main:app --reload
# Через if name = main, в командной строке python 1.py