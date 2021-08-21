from sqlalchemy import Column, Integer, String

from db.config import Base


class SdkNum(Base):
    __tablename__ = 'sdknum'

    sdk = Column(String, primary_key=True, nullable=False)
    reqnumber = Column(Integer, nullable=False)
    imprnumber = Column(Integer, nullable=False)


class UserNum(Base):
    __tablename__ = 'usernum'

    user = Column(String, nullable=False, primary_key=True)
    reqnumber = Column(Integer, nullable=False)
    imprnumber = Column(Integer, nullable=False)
