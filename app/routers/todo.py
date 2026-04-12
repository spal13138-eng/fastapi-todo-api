from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.database import SessionLocal
from app import schemas,models,utils
from app import oauth2

router=APIRouter( 
    prefix="/todos",
    tags=["Todos"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_todo(todo:schemas.TodoCreate,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):

    new_todo=models.Todo(
        title=todo.title,
        description=todo.description,
        owner_id=current_user.id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

@router.get("/",response_model=list[schemas.TodoResponse])
def get_todo(db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    todos=db.query(models.Todo)
    todos=todos.filter(models.Todo.owner_id==current_user.id).all()
  
    return todos


#@router.get("/{id}",response_model=schemas.TodoResponse)
#def get1_todo(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
#    todo_query = db.query(models.Todo).filter(
#    models.Todo.id == id,
#    models.Todo.owner_id== current_user.id
#)
#
#    if todo_query.first() is None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"todo with {id} is not found")
#    
#    return todo_query.first()

@router.put("/")
def update_todo(update_todo:schemas.TodoUpdate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    todo_query=db.query(models.Todo).filter(models.Todo.owner_id==current_user.id)


    if todo_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"todo with this {id} is not found")
    
    todo_query.update({
        "title":update_todo.title,
        "description":update_todo.description,
        "is_completed":update_todo.is_completed
    })

    db.commit()

    return {"Todo updated succesfully"}


@router.delete("/")
def delete_todo(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    todo_query=db.query(models.Todo).filter(models.Todo.owner_id==current_user.id)

    if todo_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"todo is not found")
    
    todo_query.delete(synchronize_session=False)

    db.commit()

    return {"Todo is deleted successfully"}
      