from fastapi import FastAPI

from api.routers import auth, favorite, quiz

app = FastAPI()
app.include_router(quiz.router)
app.include_router(auth.router)
app.include_router(favorite.router)
