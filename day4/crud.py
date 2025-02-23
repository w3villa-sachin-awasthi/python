from bson import ObjectId
# from models import users_collection
from schema import user_schema
from fastapi import HTTPException

async def create_user(user: user_schema):
    new_user = await user_schema.insert_one(user.dict())
    return {"id": str(new_user.inserted_id), "message": "User created successfully"}

async def get_user(id: str):
    try:
        # # print(type(id),"value of id")
        # numberid=int(id)
        # print(numberid,"number")
        # object_id = ObjectId(id)  # Convert ID to ObjectId
        user = await user_schema.find()
        print(user)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user
    except:
        raise HTTPException(status_code=400, detail="Invalid User ID format")
