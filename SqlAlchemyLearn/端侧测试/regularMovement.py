from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    text,
)

metadata_obj = MetaData()
engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

with engine.connect() as connection:
    result = connection.execute(text("select id, username from py_test pt "))
    for row in result:
        # print("id:", row["id"])
        print(row[0], row[1])

