import os
xd={
    "className":"BBlog",
    "model":"bblog",
    "models":{
        "title":"String",
        "body":"String",
        "time":"String",
    },
    "schemas":{
        "title":"str",
        "body":"str",
        "time":"str",
    
    }
}

modelsString="""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

"""
modelsString+=f"class {xd['className']}(Base):\n"
modelsString+=f"\t__tablename__='{xd['model']}'\n"
modelsString+="\tid=Column(Integer,primary_key=True , index=True)\n"
for key, value in xd['models'].items():
    modelsString+=f"\t{key}=Column({value})\n"

shemasString="""
from pydantic import BaseModel

"""
shemasString+=f"class {xd['className']}(BaseModel):\n"
for key, value in xd['schemas'].items():
    shemasString+=f"\t{key}:{value}\n"

directory = "Nikhil"
  
# Parent Directory path
parent_dir = "C:/Users/user/Desktop/school/fastapi/tut"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'Nikhil'
try:
    os.makedirs(path, exist_ok = True)
    f = open("Nikhil/__init__.py", "a")
    f.write("")
    f.close()

    f = open("Nikhil/database.py", "a")
    f.write("""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
    """)
    f.close()
    f = open("Nikhil/main.py", "a")
    f.write(f"""
from turtle import title
from fastapi import Depends, FastAPI, HTTPException, status
from . import schemas,models
from sqlalchemy.orm import Session

from .database import engine,SessionLocal
app=FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/{xd['model']}',status_code=status.HTTP_201_CREATED)
def create_{xd['model']}({xd['model']}:schemas.{xd['className']},db:Session=Depends(get_db) ):
    new_{xd['model']} =models.{xd['className']}(title={xd['model']}.title,body={xd['model']}.body)
    db.add(new_{xd['model']})
    db.commit()
    db.refresh(new_{xd['model']})
    return new_{xd['model']}

@app.get('/{xd['model']}',status_code=status.HTTP_200_OK)
def get_list_of_{xd['model']}(db:Session=Depends(get_db)):
    blogs= db.query(models.{xd['className']}).all()
    return blogs

@app.get('/{xd['model']}/{"{id}"}',status_code=status.HTTP_200_OK)
def get_single_of_{xd['model']}(id:int,db:Session=Depends(get_db)):
    blogs= db.query(models.{xd['className']}).filter(models.{xd['className']}.id==id).first()
    if not blogs:
        raise HTTPException(status_code=400,detail="{xd['className']} not found") 
    return blogs

@app.delete('/{xd['model']}/{"{id}"}',status_code=status.HTTP_204_NO_CONTENT)
def get_single_of_{xd['model']}(id:int,db:Session=Depends(get_db)):
    blogs= db.query(models.{xd['className']}).filter(models.{xd['className']}.id==id)
    if not blogs.first():
        raise HTTPException(status_code=400,detail="{xd['className']} not found")
    blogs.delete(synchronize_session=False)
    db.commit()
    return blogs
@app.put('/{xd['model']}/{"{id}"}',status_code=status.HTTP_202_ACCEPTED)
def get_single_of_{xd['model']}(id:int,{xd['model']}:schemas.{xd['className']},db:Session=Depends(get_db)):
    blogs= db.query(models.{xd['className']}).filter(models.{xd['className']}.id==id)
    if not blogs.first():
        raise HTTPException(status_code=404,detail="{xd['className']} not found")
    blogs.update({xd['model']}.dict())
    db.commit()
   
    return {xd['model']}    
    
    
    """)
    f.close()
    f = open("Nikhil/models.py", "a")
    f.write(modelsString)
    f.close()

    f = open("Nikhil/shemas.py", "a")
    f.write(shemasString)
    f.close()


    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)


