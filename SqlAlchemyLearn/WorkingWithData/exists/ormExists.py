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
    func,
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
    Column("user_id", ForeignKey("py_test.id"), nullable=False),
    Column("username", String(20)),
    Column("email_address", String, nullable=False),
)

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=True
)

"""
SELECT py_test.name 
FROM py_test 
WHERE EXISTS (SELECT count(address.id) AS count_1 
FROM address 
WHERE py_test.id = address.user_id GROUP BY address.user_id 
HAVING count(address.id) > %(count_2)s)
"""
subq = (
    select(func.count(address_table.c.id))
    .where(pytest.c.id == address_table.c.user_id)
    .group_by(address_table.c.user_id)
    .having(func.count(address_table.c.id) > 1)
).exists()

subq = (
    select(address_table.c.id).where(pytest.c.id == address_table.c.user_id)
).exists()

with engine.connect() as conn:
    result = conn.execute(select(pytest.c.name).where(subq))
    print(result.all())

    result= conn.execute(select(pytest.c.name).where(~subq))
    print(result.all())
