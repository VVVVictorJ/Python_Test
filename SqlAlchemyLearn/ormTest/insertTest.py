from typing import List, Optional

from sqlalchemy import DATETIME, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "py_test"
    id: Mapped[str] = mapped_column(String(10))
    reply: Mapped[str] = mapped_column(String(30))
    createtime: Mapped[Optional[str]] = mapped_column(String(30))

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, reply={self.reply!r}, createtime={self.createtime!r}"
        )
