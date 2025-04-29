from fastapi import FastAPI

app = FastAPI()

from api.routers import quiz

app = FastAPI()
app.include_router(quiz.router)
