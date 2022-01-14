
from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas,database,models
router=APIRouter()

@router.post("/login")
def login(req:schemas.Login,db:Session=Depends(database.get_db)):
    user= db.query(models.User).filter(models.User.email==req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"Invalid Credentials")
    return user
    