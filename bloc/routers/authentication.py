
from datetime import timedelta
from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import  OAuth2PasswordRequestForm
from bloc.token import create_access_token
from .. import schemas,database,models
from bloc.hashing import Hashing

router=APIRouter()

@router.post("/login" ,response_model=schemas.Token)
def login(req:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user= db.query(models.User).filter(models.User.email==req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"Invalid Credentials")
    if not Hashing.verify(user.password,req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"Invalid Credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token" : access_token ,"token_type":"bearer"}
    