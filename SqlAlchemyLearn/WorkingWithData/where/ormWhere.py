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
    or_,
    select,
    text,
    literal_column,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


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

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=True
)

print(pytest.c.name == "jack")

"""
SELECT py_test.id, py_test.username, py_test.name 
FROM py_test 
WHERE py_test.name = :name_1
"""
print(select(pytest).where(pytest.c.name == "jack"))

print(
    select(address_table.c.email_address)
    .where(pytest.c.name == "jack")
    .where(pytest.c.username == "victor")
)

