from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


class Item(BaseModel):
    name:str
    description:str
    price:float
    tax:float=None

@app.post("/items")
def creat_items(item:Item):
    return {"item":item}


books={
    1:{
        "id":1,
        "title":"Gorge Orwell2",
        "price":10.89
    },
    2:{
        "id":2,
        "title":"Gorge Orwell2",
        "price":20
    },
    3:{
        "id":3, 
        "title":"Gorge Orwell3",
        "price":25   
    }
}

class Book(BaseModel):
    title:str
    price:float

@app.post("/create_book/")
def create_book(book:Book):
    new_id= max(books.keys())+1
    books[new_id]={
        "id":new_id,
        "title":book.title,
        "price":book.price
    }
    return {"message":"Book Create successfully","book":book}


# how can access the particulr book using bookid, title
@app.get("/books/{book_id}")
def get_books(book_id:int):
    book= books.get(book_id)
    print("check: ",book)
    if book:
        return {"books":book}
    else:
        return {"message":"book not found"},404
