from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app=FastAPI()
class det(BaseModel):
    name: str | None = None
    age:int
    level:str

@app.get("/getuser/{name}/{age}")
def home(name:str,age:Union[int,None]=None):
    print(name,"  ",age)
    return f"value of name is {name} and value of age {age}"
@app.get("/details")
def details(details: det):
    print(details.name)
    return details
