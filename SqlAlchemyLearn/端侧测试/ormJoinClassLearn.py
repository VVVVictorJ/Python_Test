from typing import List, Optional

from sqlalchemy import (
    Column,
    ForeignKey,
    Insert,
    Integer,
    MetaData,
    String,
    Table,
    and_,
    bindparam,
    create_engine,
    func,
    or_,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Pytest(Base):
    __tablename__ = "py_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(100))
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20))
    user_id = mapped_column(ForeignKey("py_test.id"))

    user: Mapped[Pytest] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r}"


engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)


stmt = (
    select(Pytest.name, func.count(Address.id).label("count"))
    .join(Address)
    .group_by(Pytest.name)
    .having(func.count(Address.id) > 1)
)
print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())