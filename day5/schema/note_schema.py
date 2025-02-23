from pydantic import BaseModel

class notes(BaseModel):
    title:str
    description:str
    userid:str