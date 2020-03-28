from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INT, create_engine, TEXT

Base = declarative_base()


class VirusStatics(Base):
    __tablename__ = 'VirusStatics'

    id = Column(INT, primary_key=True, autoincrement=True)
    report_date = Column(String(10), comment="报导时间")
    region = Column(String(10), comment="报导时间")
    city = Column(String(10), comment="报导时间")
    new_confirm = Column(INT, comment="新增确诊")
    new_cure = Column(INT, comment="新增出院")
    new_die = Column(INT, comment="新增死亡")
    message_source = Column(String(50), comment="消息来源")
    source_url_one = Column(TEXT, comment="来源链接1")
    source_url_two = Column(TEXT, comment="来源链接2")
    source_url_three = Column(TEXT, comment="来源链接3")
    note = Column(String(150), comment="备注")


engine: Engine = create_engine('mysql+pymysql://lumia:1044740758@LumiaO:3306/VirusStatic')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
