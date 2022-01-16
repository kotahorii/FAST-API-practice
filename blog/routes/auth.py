from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, token
from ..database import get_db
from ..hashing import Hash

router = APIRouter(tags=["auth"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credential",
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password",
        )
    access_token = token.create_access_token(data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
