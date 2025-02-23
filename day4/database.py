# from motor.motor_asyncio import AsyncIOMotorClient

# # MongoDB Connection String
# MONGO_URI = "mongodb://localhost:27017"

# # Database Name
# DATABASE_NAME = "fastapi_db"

# # Create MongoDB client
# client = AsyncIOMotorClient(MONGO_URI)

# # Get database instance
# db = client[DATABASE_NAME]
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "fastapi_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

async def check_db_connection():
    try:
        await client.server_info()  # Runs a ping to check MongoDB connection
        print("db connected successfully done")
        return True
    except Exception as e:
        return False
