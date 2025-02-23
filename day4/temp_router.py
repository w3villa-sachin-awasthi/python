from fastapi import APIRouter
from pydantic import BaseModel
temp=APIRouter(
    prefix="/temp",
    tags=["temp"]
)

class Blog(BaseModel):
    name:str
    age:int
    elligible:bool

@temp.get("/{id:int}/comments")
def func(id):
    return f"hiii {type(id)}  {int(id)}"


@temp.get("/query")
def check(limit:int,published:bool):
    return f"limit is {limit} and publish is {type(published)}"

@temp.post("/check/{val1}/val1/{val2}")
def check(val1:str,val2:str,check:Blog):
    return f"{check} value one is {val1} and value of val2 {val2}"
 

#base 64 decoder   