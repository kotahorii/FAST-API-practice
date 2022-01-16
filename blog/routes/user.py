from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from ..database import get_db
from ..functions import user
from ..schemas import ShowUser, User

router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", status_code=HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get(
    "/{id}",
    response_model=ShowUser,
)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
