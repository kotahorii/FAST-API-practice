from fastapi import FastAPI

from .database import engine
from .models import Base
from .routes import auth, blog, user

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

Base.metadata.create_all(engine)
