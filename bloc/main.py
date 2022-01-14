
from fastapi import  FastAPI
from .routers import blog,user
from . import models
from .database import engine
app=FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["blogs"])
# def create_blog(blog:schemas.Blog,db:Session=Depends(get_db) ):
#     new_blog =models.Blog(title=blog.title,body=blog.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[schemas.showBlog],tags=["blogs"])
# def get_list_of_blog(db:Session=Depends(get_db)):
#     blogs= db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.showBlog,tags=["blogs"])
# def get_single_of_blog(id:int,db:Session=Depends(get_db)):
#     blogs= db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blogs:
#         raise HTTPException(status_code=400,detail="Blog not found") 
#     return blogs

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
# def get_single_of_blog(id:int,db:Session=Depends(get_db)):
#     blogs= db.query(models.Blog).filter(models.Blog.id==id)
#     if not blogs.first():
#         raise HTTPException(status_code=400,detail="Blog not found")
#     blogs.delete(synchronize_session=False)
#     db.commit()
#     return blogs
# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
# def get_single_of_blog(id:int,blog:schemas.Blog,db:Session=Depends(get_db)):
#     blogs= db.query(models.Blog).filter(models.Blog.id==id)
#     if not blogs.first():
#         raise HTTPException(status_code=404,detail="Blog not found")
#     blogs.update(blog.dict())
#     db.commit()
   
#     return blog





