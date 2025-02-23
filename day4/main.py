from fastapi import FastAPI
from user_router import users
from database import check_db_connection
from temp_router import temp
app=FastAPI()


app.include_router(users)
app.include_router(temp)
@app.get("/health/")
async def health_check():
    db_status = await check_db_connection()
    return {"database_connected": db_status}