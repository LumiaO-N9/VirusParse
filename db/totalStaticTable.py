from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INT, create_engine

Base = declarative_base()


class TotalStatic(Base):
    __tablename__ = 'totalStatic'

    id = Column(INT, primary_key=True, autoincrement=True)
    region = Column(String(10), comment="报导时间")
    total_confirm = Column(INT, comment="总计确诊")
    total_cure = Column(INT, comment="总计出院")
    total_die = Column(INT, comment="总计死亡")

engine: Engine = create_engine('mysql+pymysql://lumia:1044740758@LumiaO:3306/VirusStatic')
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
