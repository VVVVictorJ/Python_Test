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
    literal_column,
    or_,
    select,
    text,
    union_all,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    aliased,
    mapped_column,
    relationship,
)

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
    Column("user_id", ForeignKey("py_test.id"), nullable=False),
    Column("username", String(20)),
    Column("email_address", String, nullable=False),
)


class Base(DeclarativeBase):
    pass


class Pytest(Base):
    __tablename__ = "py_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(100))
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"Pytest(id={self.id!r}, name={self.name!r}, username={self.username!r})"


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
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=True
)

stmt1 = select(pytest).where(pytest.c.name == "sandy")
stmt2 = select(pytest).where(pytest.c.name == "spongebob")
u = union_all(stmt1, stmt2)
# with engine.connect() as conn:
#     result = conn.execute(u)
#     print(result.all())

stmt1 = select(Pytest).where(Pytest.name == "jack")
stmt2 = select(Pytest).where(Pytest.name == "sandy")
u = union_all(stmt1, stmt2)

"""
从联合中选择ORM实体 
Select.from_statement() 方法
使用 Select.from_statement() 后不能添加额外的条件
"""
user_alias = aliased(Pytest, u.subquery())
orm_stmt = select(Pytest).from_statement(u)
with Session(engine) as session:
    for obj in session.execute(orm_stmt).scalars():
        print(obj)

"""
CompoundSelect.subquery()
CompoundSelect 构造组织到子查询中，然后使用 aliased() 链接到 ORM 对象功能。
UNION 本身之外添加其他条件，例如 ORDER BY，因为我们可以按子查询导出的列进行过滤或排序
"""
user_alias = aliased(Pytest, u.subquery())
orm_stmt = select(user_alias).order_by(user_alias.id)
with Session(engine) as session:
    for obj in session.execute(orm_stmt).scalars():
        print(obj)
