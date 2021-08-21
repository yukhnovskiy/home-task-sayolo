from fastapi import FastAPI
from pydantic import BaseModel

from db.config import engine, Base


class SdkNum(BaseModel):
    sdk_version: str
    reqnumber: int


class UserNum(BaseModel):
    user_name: str
    reqnumber: int


app = FastAPI(title="Async FastAPI")


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
