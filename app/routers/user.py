from fastapi import APIRouter,Depends,HTTPException,status

from app.database import get_db
from app import models,schemas
from app import oauth2
from sqlalchemy.orm import Session
from app import utils

router=APIRouter(
    prefix="/register",
    tags=["user"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}",response_model=schemas.UserOut)
def getuser(id:int,db:Session=Depends(get_db)):

    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with {id} is not found")  
    

    return user
