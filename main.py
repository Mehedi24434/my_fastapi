from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()
@app.get("/blog")
def blog(limit, published:bool=True):
    if published:
        return {'data':f'{limit} published blogs in list of limit'}
    else:
        return {'data': f'{limit} blogs in list of limit'}

@app.get("/blog/{id}")

def show(id:int):

    # fetch blog with id = id
    return {'data':id}
@app.get("/blog/{id}/comments")
def comments(id):
    # fetch blog with comments id = id
    return {'data':{'comments':id+" num comment"}}
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]              
@app.post('/blog')

def create_blog(blog:Blog):
    return {'data':f'the Blog is created as per {blog.title}'}    

