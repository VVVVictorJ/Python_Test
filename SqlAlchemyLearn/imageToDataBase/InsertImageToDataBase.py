# 使用sqlalchemy将1.jpg存入mysql
#     使用sqlalchemy将1.jpg存入mysql数据库

import random

from sqlalchemy import LargeBinary, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker

Base = declarative_base()


class Image(Base):
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(primary_key=True)
    img_name: Mapped[str] = mapped_column(String(255))
    img: Mapped[str] = mapped_column(LargeBinary)

    def __init__(self, img_name, img, uuid):
        self.img_name = img_name
        self.img = img
        self.id = uuid

    def __repr__(self):
        return "<Image('%s', '%s')>" % (self.img_name, self.img)

    # 写一个自动生成随机正整数的函数

    def write_to_db():
        engine = create_engine(
            "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8",
            echo=True,
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        # 读取图片
        with open("1.jpg", "rb") as f:
            img = f.read()
        # 写入数据库
        image = Image("1.jpg", img, random.randint(1, 999999999))
        session.add(image)
        session.commit()
        session.close()

    def read_from_db():
        engine = create_engine(
            "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8",
            echo=True,
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        # 读取数据库
        img = session.query(Image).filter_by(img_name="1.jpg").first()
        # 写入图片
        with open("3.jpg", "wb") as f:
            f.write(img.img)
        session.close()


if __name__ == "__main__":
    Image.write_to_db()
    Image.read_from_db()
