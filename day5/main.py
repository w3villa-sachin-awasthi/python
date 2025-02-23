from fastapi import FastAPI
from routes.userroutes import users
app=FastAPI()

app.include_router(users)