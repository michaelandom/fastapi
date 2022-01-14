from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas


def get_all(db:Session):
    blogs= db.query(models.Blog).all()
    return blogs

def create_blog(blog:schemas.Blog,db:Session):
    new_blog =models.Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_single_blog(id:int,db:Session):
    blogs= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=400,detail="Blog not found") 
    return blogs

def delete_single(id:int,db:Session):
    blogs= db.query(models.Blog).filter(models.Blog.id==id)
    if not blogs.first():
        raise HTTPException(status_code=400,detail="Blog not found")
    blogs.delete(synchronize_session=False)
    db.commit()
    return blogs

def update_single_blog(id:int,blog:schemas.Blog,db:Session):
    blogs= db.query(models.Blog).filter(models.Blog.id==id)
    if not blogs.first():
        raise HTTPException(status_code=404,detail="Blog not found")
    blogs.update(blog.dict())
    db.commit()
