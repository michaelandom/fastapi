from typing import Optional
from fastapi import FastAPI

app=FastAPI()

@app.get('/blog')
def index(limit:int=10,published:bool=False,sort:str | None=None):
    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return {'data' : f'{limit} blog from the db'}

@app.get('/about')
def about():
    return {'data':"micahel fast "}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':"unpublished"}


@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int,limit:int=10):
    return {'data':{id,limit}}

