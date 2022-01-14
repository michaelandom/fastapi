from http.client import HTTPException
from fastapi import APIRouter,status,Depends

from bloc.hashing import Hashing
from  .. import schemas ,database,models
from sqlalchemy.orm import Session
from bloc.respository import user
from typing import List
router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.showUser,)
def create_user(user:schemas.User,db:Session=Depends(database.get_db)):
    return user.create_user(user,db)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.showUser],)
def get_users(db:Session=Depends(database.get_db)):
    return user.get_all_users(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.showUser,)
def get_user(id:int,db:Session=Depends(database.get_db)):
    return user.get_single_user(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.showUser,)
def update_user(id:int,req:schemas.User,db:Session=Depends(database.get_db)):
    return user.update_single_users(id,req,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def delete_user(id:int,db:Session=Depends(database.get_db)):
    return user.delete_single_user(id,db)