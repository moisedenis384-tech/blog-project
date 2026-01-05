from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 

# in memory storage of items
Items = []

# base model definition and field structure
class Item(BaseModel):
    name :str 
    price : int

app = FastAPI(root_path = "/api/v1")

# creating a item  of type Item 
@app.post("/new-item")
async def create_item(item:Item):
 Items.append(item)
 return {"added Item":item}

# getting all created items 
@app.get("/all-items")
async def all_items():
    return {"Items":Items}

# getting a specific item 
@app.get("/get-item/{item_id}")
async def get_item(item_id:int):
   for i in Items :
       return {"items":Items[item_id]}
   raise HTTPException(status_code = 404) 

# updating a specific item 
@app.put("/update-item/{item_id}")
async def update_item(item_id:int , item : Item):
   Items[item_id] = item  
   return {"items":item} 

# deleting a specific item 
@app.delete("/delete_item/{item_id}")
async def delete_item(delete_id :int):
   delete_id = Items.pop(delete_id)
   return {"deleted item":delete_id}