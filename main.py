from fastapi import FastAPI,Body,HTTPException,status
from pydantic import BaseModel
from typing import Annotated
from db import mycol
from fastapi.middleware.cors import CORSMiddleware



class FormData(BaseModel):
    fullName:str
    email:str
    phoneNumber:str
    feedBack:str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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