from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import models
from .database import engine
from .routers import posts, details


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "API is successfully connected"}


app.include_router(posts.router)
app.include_router(details.router)

# https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb
