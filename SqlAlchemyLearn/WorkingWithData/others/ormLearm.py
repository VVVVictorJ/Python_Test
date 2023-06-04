from typing import List, Optional

from sqlalchemy import (
    Column,
    ForeignKey,
    Insert,
    Integer,
    MetaData,
    String,
    Table,
    bindparam,
    create_engine,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Pytest(Base):
    __tablename__ = "py_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(20))
    user_id = mapped_column(ForeignKey("py_test.id"))

    user: Mapped[Pytest] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r}"


# test = Pytest(id=3, username="jack")

# stmt = Insert(Pytest).values(id=5, username="")

# INSERT INTO py_test (id, username) VALUES (:id, :username)
# print(stmt)

# 字符串形式通过生成对象的编译形式创建的，该对象包括语句的特定于数据库的字符串SQL表示
# 可以ClauseElement.complie()方法获取这个对象。
# complied = stmt.compile()

# {'id': 5, 'username': ''}
# print(complied.params)

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=True
)

# with engine.connect() as conn:
#     result = conn.execute(
#         Insert(Pytest),
#         [{"id": 6, "username": "jackson"}, {"id": 7, "username": "gove"}],
#     )
#     conn.commit()

# 创建表
# Base.metadata.create_all(engine)

stmt = Insert(Pytest).values(id=100, username="jack")
# print(stmt)
complied = stmt.compile()

metadata_obj = MetaData()

pytest = Table(
    "py_test",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30)),
    Column("name", String(100)),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("pytest.id"), nullable=False),
    Column("username", String(20)),
    Column("email_address", String, nullable=False),
)

scalar_subq = select(pytest.c.id).where(pytest.c.username == "victor").scalar_subquery()

# insert_stmt = (
#     Insert(address_table)
#     .values(user_id=2, email_address="abc@163.com")
#     .returning(
#         address_table.c.user_id,
#         address_table.c.email_address,
#         address_table.c.id
#     )
# )

with engine.connect() as conn:
    # result = conn.execute(stmt)
    # CursorResult.inserted_primary_key 返回一个元组，因为主键可能包含多个列。
    # print(result.inserted_primary_key)

    result = conn.execute(
        Insert(address_table).values(user_id=scalar_subq),
        [
            {
                "username": "spongebob",
                "email_address": "spongebob@sqlalchemy.org",
            },
            {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
            {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
        ],
    )
    # result = conn.execute(insert_stmt)
    conn.commit()
