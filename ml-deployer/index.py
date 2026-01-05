from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 



app = FastAPI(root_path ="/api/v2")


class Book(BaseModel):
    title : str 
    author : str
    description : str
    price : float 


Books = [] 


@app.get("/books")
async def all_books():
    return {"all books":Books} 


@app.get("/books/{book_id}")
async def single_book(book_id:int):
    for i in Books :
     book_id = Books[book_id]
     return {"wanted Book":book_id}
    raise HTTPException(status_code = 404)


@app.post("/books")
async def create_book(book:Book):
    Books.append(book) 
    return {"new Book":book}

    
@app.put("/books/{book_id}")
async def update_book(book_id :int ,book :Book) :
   Books[book_id] = book
   return {"updated book":book}

@app.delete("/books") 
async def delete_book(book_id:int):
   book_id = Books.pop(book_id)
   return {"deleted book":book_id}