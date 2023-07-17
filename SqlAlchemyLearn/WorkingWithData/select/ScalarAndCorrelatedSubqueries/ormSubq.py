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
(SELECT count(address.id) AS count_1 
FROM address, py_test 
WHERE py_test.id = address.user_id)
"""
subq = (
    select(func.count(address_table.c.id))
    .where(pytest.c.id == address_table.c.user_id)
    .scalar_subquery()
)

print(subq)

"""
(SELECT count(address.id) AS count_1 
FROM address, py_test 
WHERE py_test.id = address.user_id) = :param_1
"""
print(subq == 5)


"""
SELECT py_test.name, (SELECT count(address.id) AS count_1 
FROM address 
WHERE py_test.id = address.user_id) AS address_count 
FROM py_test
"""
stmt = select(pytest.c.name, subq.label("address_count"))

print(stmt)

subq = (
    select(func.count(address_table.c.id))
    .where(pytest.c.id == address_table.c.user_id)
    .scalar_subquery()
    .correlate(pytest)
)

with engine.connect() as conn:
    result = conn.execute(
        select(
            pytest.c.name,
            address_table.c.email_address,
            subq.label("address_count"),
        )
        .join_from(pytest, address_table)
        .order_by(pytest.c.id, address_table.c.id)
    )
    print(result.all())
