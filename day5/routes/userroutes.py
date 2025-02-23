# from fastapi import APIRouter
# from models.users import users
# users=APIRouter(prefix="/users",tags=["users"])

# @users.get("/")
# async def func():
#     response=await users.find()
#     print("responses ----- ",response)
#     return f"responses are {response}"

# @users.get("/user")
# def func():
#     return "you are getting one a single users"
from fastapi import APIRouter
from models.users import users as users_collection  # Avoid overwriting

users = APIRouter(prefix="/users", tags=["users"])

@users.get("/")
async def get_all_users():
    response = await users_collection.find().to_list(None)  # Convert cursor to list
    return {"responses": response}

@users.get("/user")
async def get_single_user():
    return {"message": "You are getting a single user"}
