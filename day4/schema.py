from pydantic import BaseModel
class user_schema(BaseModel):
    name:str
    age:int
    