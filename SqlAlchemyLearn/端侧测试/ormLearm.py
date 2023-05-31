from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import Insert, create_engine


class Base(DeclarativeBase):
    pass


class Pytest(Base):
    __tablename__ = "py_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))


# test = Pytest(id=3, username="jack")

stmt = Insert(Pytest).values(id=5, username="")

print(stmt)

complied = stmt.compile()

print(complied.params)

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     print(result)
#     result.inserted_primary_key
#     conn.commit()

with engine.connect() as conn:
    result = conn.execute(
        Insert(Pytest),
        [
            {"id":6, "username": "jackson"},
            {"id":7, "username": "gove"}
        ]
    )
    conn.commit()