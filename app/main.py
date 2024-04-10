from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World ALL"}


app.include_router(posts.router)

# https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb
