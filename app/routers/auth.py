from fastapi import APIRouter,Depends,HTTPException,status
from app.database import get_db,SessionLocal
from app import schemas
from app import utils
from app import models
from sqlalchemy.orm import Session
from app.routers import auth
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from app import oauth2


router=APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.get("/test")
def test():
    return {"Auth route is working"}

@router.post("/")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid credentials")
    

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid credentials")
    

    access_token=oauth2.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token,"token_type":"bearer"}

    


    



