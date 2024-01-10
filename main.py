from fastapi import FastAPI,Body,HTTPException,status
from pydantic import BaseModel
from typing import Annotated
from db import mycol

class FormData(BaseModel):
    fullName:str
    email:str
    phoneNumber:str
    feedBack:str


app = FastAPI()



@app.post("/from/submit")
async def root(formData:Annotated[FormData,Body()]):
    print(dict(formData))
    try:
        data=mycol.insert_one(formData.model_dump())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Internal Server Error")
    return {
        "success":True,
    }