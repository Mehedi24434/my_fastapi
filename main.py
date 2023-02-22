from typing import Union
from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hi I am Mehedi"}
@app.get("/about")
def about():
    return {'data':{'name':'Mehedi'}}
