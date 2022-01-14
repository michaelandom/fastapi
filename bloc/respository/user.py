from fastapi import HTTPException
from sqlalchemy.orm import Session
from bloc.hashing import Hashing
from .. import models,schemas


def create_user(user:schemas.User,db:Session):
    new_user=models.User(name=user.name,email=user.email,password=Hashing.bCrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    users=db.query(models.User).all()
    return users

def get_single_user(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first();
    if not user:
        raise( HTTPException(status_code=404,detail="user not found"))
    return user

def update_single_users(id:int,req:schemas.User,db:Session):
    user=db.query(models.User).filter(models.User.id==id)
    old_user=user.first()
    if not old_user:
        raise( HTTPException(status_code=404,detail="user not found"))
    user.update(req.dict())
    db.commit()
    db.refresh(old_user)
    return old_user
    
def delete_single_user(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise( HTTPException(status_code=404,detail="user not found"))
    user.delete(synchronize_session=False)
    db.commit()
    return "ok"