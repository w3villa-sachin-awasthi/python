from fastapi import APIRouter
from crud import create_user, get_user
# from schemas import UserSchema

users = APIRouter(prefix="/users", tags=["Users"])

@users.post("/")
async def create_new_user():
    return await create_user()

@users.get("/{user_id}")
async def get_user_by_id(user_id: str):
    return await get_user(user_id)
