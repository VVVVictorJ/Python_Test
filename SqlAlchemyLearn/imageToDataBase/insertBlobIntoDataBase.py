from typing import List

from sqlalchemy import (
    Column,
    ForeignKey,
    Insert,
    Integer,
    LargeBinary,
    MetaData,
    String,
    Table,
    create_engine,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# class TestDocx(Base):
#     __tablename__ = "testdocx"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     docx_id: Mapped[str] = mapped_column(String(20))
#     images: Mapped[List["TestImage"]] = relationship(back_populates="")


class TestImage(Base):
    __tablename__ = "testimage"
    id: Mapped[int] = mapped_column(primary_key=True)
    # docx_id: Mapped[str] = mapped_column(ForeignKey("testdocx.id"))
    image_blob: Mapped[str] = mapped_column(LargeBinary)
    # docx: Mapped[TestDocx] = relationship(back_populates="images")


metadata_obj = MetaData()

# test_docx = Table("testdocxqin")

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8", echo=False
)

# mediumblob 存储的是二进制数据
# 故直接提供打开文件的二进制数据
with open("1.png", "rb") as f:
    img = f.read()

# print(img)

stmt = select(TestImage.image_blob).filter_by(id=1)

with engine.connect() as conn:
    rows = conn.execute(stmt)
    for row in rows:
        # print(row[0])
        with open("2.png", "wb") as f:
            f.write(row[0])

    # 直接把对象赋值给对应的字段即可
    # result = conn.execute(
    #     Insert(TestImage).values(
    #         id=1, image_blob=img
    #     )
    # )
    conn.commit()
