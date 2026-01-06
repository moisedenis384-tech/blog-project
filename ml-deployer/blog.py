from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 

app = FastAPI(root_path="/api/v3") 

class Post(BaseModel):
    desc :str = None 
    author :str 

Posts = [] 


@app.post("/posts")
async def create_post(post :Post):
    Posts.append(post) 
    return {"created post":post} 


@app.get("/posts")
async def all_posts():
    return{"all posts ":Posts}
    

@app.get("/posts/{posts_id}")
async def single_post(post_id :int ):
    if post_id < 0 or post_id >= len(Posts):
        raise HTTPException(status_code = 404 , detail ="post not found")
    
    post_id = Posts[post_id]
    return {"the post is ":post_id} 
    

@app.put("/posts/{posts_id}")
async def update_post(post_id :int, post:Post): 
    if post_id < 0 or post_id >= len(Posts):
        raise HTTPException(status_code = 404 , detail ="post not found")
    Posts[post_id]= post 
    return {"update post":post}


@app.delete("/posts/{post_id}")
async def delete_post(post_id:int):
    if post_id < 0 or post_id >= len(Posts):
        raise HTTPException(status_code = 404 , detail ="post not found")
    post_id = Posts.pop(post_id) 
    return {"deleted post":post_id}
