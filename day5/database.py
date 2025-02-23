# from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_URL = "mongodb://localhost:27017"  # Change if needed
# client = AsyncIOMotorClient(MONGO_URL)

# db = client["mydatabase"]  # Your MongoDB database name


from motor.motor_asyncio import AsyncIOMotorClient
Mongo_url="mongodb://localhost:27017"
client=AsyncIOMotorClient(Mongo_url)

db=client['fastapi_db']
