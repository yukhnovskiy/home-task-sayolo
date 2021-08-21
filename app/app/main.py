import requests
import uvicorn
from fastapi import responses, status

from app import app
from dal.sdk_dal import SdkNumDAL
from dal.user_dal import UserNumDAL
from db.config import async_session


@app.get("/getad/")
async def get_request(sdk_version: str, session_id: int, platform: str, user_name: str, country_code: str):
    req = requests.get('https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast')
    xml_cont = req.content
    resp = responses.Response(content=xml_cont, media_type='application/xml')
    sdk_req = await get_sdk_req(sdk_version)
    sdk_impr = await get_sdk_impr(sdk_version)

    if sdk_req == 0 and sdk_impr == 0:
        await create_sdk_req(sdk_version, 1)
    else:
        await update_sdk_req(sdk_version, int(sdk_req) + 1)

    user_req = await get_user_req(user_name)
    user_impr = await get_user_impr(user_name)

    if user_impr == 0 and user_req == 0:
        await create_user_req(user_name, 1)
    else:
        await update_user_req(user_name, int(user_req) + 1)

    return (resp)


@app.get("/impression/", status_code=status.HTTP_200_OK)
async def get_request(sdk_version: str, session_id: int, platform: str, user_name: str, country_code: str):
    sdk_req = await get_sdk_req(sdk_version)
    sdk_impr = await get_sdk_impr(sdk_version)

    if sdk_req == 0 and sdk_impr == 0:
        await create_sdk_impr(sdk_version, 1)
    else:
        await update_sdk_impr(sdk_version, int(sdk_impr) + 1)

    user_impr = await get_user_impr(user_name)
    user_req = await get_user_req(user_name)

    if user_req == 0 and user_impr == 0:
        await create_user_impr(user_name, 1)
    else:
        await update_user_impr(user_name, int(user_impr) + 1)

    return {"status": status.HTTP_200_OK}


# async method for creating sdk request db
async def create_sdk_req(sdk: str, num: int):
    async with async_session() as session:
        async with session.begin():
            sdk_dal = SdkNumDAL(session)
            return await sdk_dal.create_sdk_req(sdk, num)


# async method for creating sdk impression db
async def create_sdk_impr(sdk: str, num: int):
    async with async_session() as session:
        async with session.begin():
            sdk_dal = SdkNumDAL(session)
            return await sdk_dal.create_sdk_impr(sdk, num)


# async method for getting sdk request num from db
def get_sdk_req(sdk: str) -> int:
    session = async_session()
    session.begin()
    sdk_dal = SdkNumDAL(session)
    return sdk_dal.get_sdk_num_req(sdk)


# async method for getting sdk impression num from db
def get_sdk_impr(sdk: str) -> int:
    session = async_session()
    session.begin()
    sdk_dal = SdkNumDAL(session)
    return sdk_dal.get_sdk_num_impr(sdk)


# async method for updating sdk request num in db
async def update_sdk_req(sdk: str, num: int):
    async with async_session() as session:
        async with session.begin():
            sdk_dal = SdkNumDAL(session)
            return await sdk_dal.update_sdk_req(sdk, num)


# async method for updating sdk impression num in db
async def update_sdk_impr(sdk: str, num: int):
    async with async_session() as session:
        async with session.begin():
            sdk_dal = SdkNumDAL(session)
            return await sdk_dal.update_sdk_impr(sdk, num)


# async method for creating user request in db
async def create_user_req(user: str, num: int):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.create_user_req(user, num)


# async method for creating user impression in db
async def create_user_impr(user: str, num: int):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.create_user_impr(user, num)


# async method for getting request num from db
async def get_user_req(user: str) -> int:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.get_user_num_req(user)


# async method for getting impression num from db
async def get_user_impr(user: str) -> int:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.get_user_num_impr(user)


# async method for updating request num in db
async def update_user_req(user: str, num: int):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.update_user_req(user, num)


# async method for updating impression num in db
async def update_user_impr(user: str, num: int):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserNumDAL(session)
            return await user_dal.update_user_impr(user, num)

@app.get("/")
def read_root():
    return {"Welcome": "Sayolo"}

#for starting server from IDE uncomment lines and run python main.py
#if __name__ == "__main__":
#    uvicorn.run("app:app", host="127.0.0.1", port=80)
