import datetime
import decimal
import random
from typing import Any, List, Optional

from sqlalchemy import DATETIME, DECIMAL, ForeignKey, String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "py_test"
    id: Mapped[int] = mapped_column(primary_key=True)
    reply: Mapped[str] = mapped_column(String(30))
    createtime: Mapped[Optional[str]] = mapped_column(String(30))
    count: Mapped[decimal.Decimal]

    def __init__(self, reply, createtime, count, **kw: Any):
        self.reply = reply
        self.createtime = createtime
        self.count = count
        
    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, reply={self.reply!r}, createtime={self.createtime!r}"
        )


# 生成插入decimal数据的sql语句

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8",
    echo=True,
)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
test = Test("test", datetime.datetime.now(), 1.1)
session.add(test)
session.commit()
session.close()