from sqlalchemy import update
from sqlalchemy.orm import Session

from db.models.models import SdkNum


class SdkNumDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_sdk_req(self, sdk: str, num: int):
        new_sdk = SdkNum(sdk=sdk, reqnumber=num, imprnumber=0)
        self.db_session.add(new_sdk)
        await self.db_session.flush()

    async def create_sdk_impr(self, sdk: str, num: int):
        new_sdk = SdkNum(sdk=sdk, reqnumber=0, imprnumber=num)
        self.db_session.add(new_sdk)
        await self.db_session.flush()

    async def update_sdk_req(self, sdk: str, pnum: int):
        q = update(SdkNum).where(SdkNum.sdk == sdk)
        q = q.values(reqnumber=pnum)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)

    async def update_sdk_impr(self, sdk: str, pnum: int):
        q = update(SdkNum).where(SdkNum.sdk == sdk)
        q = q.values(imprnumber=pnum)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)

    async def get_sdk_num_req(self, psdk: str) -> int:
        q = await self.db_session.execute(f'Select reqnumber from sdknum where sdk = "{psdk}"')
        value = q.scalars().all()
        return 0 if len(value) == 0 else value[0]

    async def get_sdk_num_impr(self, psdk: str) -> int:
        q = await self.db_session.execute(f'Select imprnumber from sdknum where sdk = "{psdk}"')
        value = q.scalars().all()
        return 0 if len(value) == 0 else value[0]
