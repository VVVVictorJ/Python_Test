from typing import List, Optional
import datetime
import decimal

from sqlalchemy import DATETIME, ForeignKey, String, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "py_test"
    id: Mapped[int] = mapped_column(primary_key=True)
    reply: Mapped[str] = mapped_column(String(30))
    createtime: Mapped[Optional[str]] = mapped_column(String(30))
    count:Mapped[decimal.Decimal]

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, reply={self.reply!r}, createtime={self.createtime!r}"
        )

# 生成插入decimal数据的sql语句

a = datetime.date
b = decimal.Decimal
print(a, b)
