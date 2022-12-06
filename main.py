from fastapi import FastAPI
from routers import predictions
from auth import authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(predictions.router)
