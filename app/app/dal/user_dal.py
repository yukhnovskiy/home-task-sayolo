from sqlalchemy import update
from sqlalchemy.orm import Session

from db.models.models import UserNum


class UserNumDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_user_req(self, pname: str, num: int):
        new_user = UserNum(user=pname, reqnumber=num, imprnumber=0)
        self.db_session.add(new_user)
        await self.db_session.flush()

    async def create_user_impr(self, pname: str, num: int):
        new_user = UserNum(user=pname, reqnumber=0, imprnumber=num)
        self.db_session.add(new_user)
        await self.db_session.flush()

    async def update_user_req(self, pname: str, pnum: int):
        q = update(UserNum).where(UserNum.user == pname)
        q = q.values(reqnumber=pnum)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

    async def update_user_impr(self, pname: str, pnum: int):
        q = update(UserNum).where(UserNum.user == pname)
        q = q.values(imprnumber=pnum)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

    async def get_user_num_req(self, pname: str) -> int:
        q = await self.db_session.execute(f"Select reqnumber from usernum where user = '{pname}'")
        value = q.scalars().all()
        return 0 if len(value) == 0 else value[0]

    async def get_user_num_impr(self, pname: str) -> int:
        q = await self.db_session.execute(f"Select imprnumber from usernum where user = '{pname}'")
        value = q.scalars().all()
        return 0 if len(value) == 0 else value[0]
