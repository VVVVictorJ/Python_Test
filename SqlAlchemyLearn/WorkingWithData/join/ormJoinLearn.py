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

"""
SqlAlchemy 对象式查询
Join 练习
"""

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
    # 此处需注意是py_test.id, 真实表名.字段名
    Column("user_id", ForeignKey("py_test.id"), nullable=False),
    Column("username", String(20)),
    Column("email_address", String, nullable=False),
)

print(select(pytest.c.name))

# 自动全连接
print(select(pytest.c.name, address_table.c.email_address))

print(
    select(pytest.c.name, address_table.c.email_address).join_from(
        pytest, address_table
    )
)

# 仅指示JOIN的右侧，推断左侧
print(select(pytest.c.name, address_table.c.email_address).join(address_table))

print(select(func.count("*")).select_from(pytest))

# 连接
print(
    select(address_table.c.email_address)
    .select_from(pytest)
    .join(address_table, pytest.c.id == address_table.c.user_id)
)

# outer join
print(select(pytest).join(address_table, isouter=True))

# full join
print(select(pytest).join(address_table, full=True))

"""
order by
group by 
having
"""

print(select(pytest).order_by(pytest.c.username))

# 升/降序
print(select(pytest).order_by(pytest.c.username.desc()))

print(
    select(address_table.c.email_address)
    .select_from(pytest)
    .join(address_table, pytest.c.id == address_table.c.user_id)
)

