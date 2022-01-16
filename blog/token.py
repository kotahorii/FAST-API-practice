from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from sqlalchemy.orm import Session

from .functions.user import show

SECRET_KEY = "efe08c92decfa8709c2f9acd8ada4bef87d7fe40e89f647cd4b9b0c4c6c0dbf5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_expection, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: int = payload.get("id")
        if email is None:
            raise credentials_expection
    except JWTError:
        raise credentials_expection
    user = show(id, db)
    return user
