from typing import Text

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(request_password: str, user_password: Text):
        return pwd_context.verify(request_password, user_password)
