from http.client import HTTPException
from fastapi import APIRouter,status,Depends

from bloc.respository import blog
from  .. import schemas ,database,models
from sqlalchemy.orm import Session
from typing import List
router=APIRouter(
    prefix="/blog",
    tags=["Blogs"]
    
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=List[schemas.showBlog])
def create_blog(req:schemas.Blog,db:Session=Depends(database.get_db)):
    return blog.create_blog(req,db)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.showBlog])
def get_list_of_blog(db:Session=Depends(database.get_db)):
   return  blog.get_all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.showBlog)
def get_single_of_blog(id:int,db:Session=Depends(database.get_db)):
  return  blog.get_single_blog(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def get_single_of_blog(id:int,db:Session=Depends(database.get_db)):
   return blog.delete_single(id,db)
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def get_single_of_blog(id:int,req:schemas.Blog,db:Session=Depends(database.get_db)):
   return blog.update_single_blog(id,req,db)
   