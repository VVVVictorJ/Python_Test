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
    Column("user_id", ForeignKey("py_test.id"), nullable=False),
    Column("username", String(20)),
    Column("email_address", String, nullable=False),
)

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=True
)


"""
SELECT ? || pytest.name AS username
FROM pytest ORDER BY pytest.name
"""
stmt = select(
    ("Username:" + pytest.c.name).label("username"),
).order_by(pytest.c.name)

"""
SELECT 'some phrase', py_test.name 
FROM py_test ORDER BY py_test.name
"""
stmt2 = select(text("'some phrase'"), pytest.c.name).order_by(pytest.c.name)

"""
SELECT 'some phrase' AS p, py_test.name 
FROM py_test ORDER BY py_test.name
"""
stmt3 = select(literal_column("'some phrase'").label("p"), pytest.c.name).order_by(
    pytest.c.name
)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username}")
    print(conn.execute(stmt2).all())
    for row in conn.execute(stmt3):
        print(f"{row.p}, {row.name}")
