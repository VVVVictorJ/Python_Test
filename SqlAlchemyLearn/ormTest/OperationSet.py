import decimal
import random

from sqlalchemy import LargeBinary, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class DCYW0020(Base):
    __tablename__ = "tdcyw0020"
    ERROR_REPORT_FILE_ID: Mapped[str] = mapped_column(
        String(100), primary_key=True
    )  # 故障报告书编码
    ERROR_EQUIPMENT_NAME: Mapped[str] = mapped_column(String(30))  # 设备名称（故障系统）
    ERROR_RESPONSIBILITY_AREA: Mapped[str] = mapped_column(String(30))  # 运维区域
    ERROR_START_TIME: Mapped[str] = mapped_column(String(30))  # 处理开始时间
    ERROR_END_TIME: Mapped[str] = mapped_column(String(30))  # 处理结束时间
    ERROR_SHUTDOWN_START_TIME: Mapped[str] = mapped_column(String(30))  # 系统主机停机开始时间
    ERROR_SHUTDOWN_END_TIME: Mapped[str] = mapped_column(String(30))  # 系统主机停机结束时间
    ERROR_EFFECT_BUSINESS_START_TIME: Mapped[str] = mapped_column(
        String(30)
    )  # 影响业务开始时间
    ERROR_EFFECT_BUSINESS_END_TIME: Mapped[str] = mapped_column(String(30))  # 影响业务结束时间
    ERROR_SHUTDOWN_PERIOD: Mapped[decimal.Decimal]  # 系统主机停机历时
    ERROR_EFFECT_BUSINESS_PERIOD: Mapped[decimal.Decimal]  # 影响业务历时
    ERROR_PHENOMENON: Mapped[str] = mapped_column(String(1000))  # 故障现象
    ERROR_SHORTCUT_DESCRIPTION: Mapped[str] = mapped_column(String(255))  # 故障简述
    ERROR_PROPERTY: Mapped[str] = mapped_column(
        String(20)
    )  # 故障属性（01 业务  02 生产 03 业务&&生产）
    ERROR_HAPPEN_DATE: Mapped[30] = mapped_column(String(30))  # 故障时间
    ERROR_REASON: Mapped[str] = mapped_column(String(1000))  # 故障原因
    ERROR_INSPECTION: Mapped[str] = mapped_column(String(1000))  # 排障过程
    ERROR_CONSUME_BACKUP: Mapped[str] = mapped_column(String(100))  # 消耗备件
    ERROR_PROCESSORS: Mapped[str] = mapped_column(String(40))  # 故障处理人
    ERROR_TAKE_CHARGE: Mapped[str] = mapped_column(String(100))  # 责任方
    ERROR_CORRECTIVE_ACTION_AND_PREVENTION_MEASURES: Mapped[str] = mapped_column(
        String(1000)
    )  # 纠正措施及预防措施#
    REC_CREATE_TIME: Mapped[str] = mapped_column(String(40))  # 创建时间
    REC_CREATOR: Mapped[str] = mapped_column(String(10))  # 记录创建者
    REC_REVISE_TIME: Mapped[str] = mapped_column(String(40))  # 记录更新时间
    RECORD_REVISE_COUNT: Mapped[int]  # 记录更新次数
    REC_REVISOR: Mapped[str] = mapped_column(String(10))  # 记录更新者

    def __init__(
        self,
        ERROR_REPORT_FILE_ID,
        ERROR_EQUIPMENT_NAME,
        ERROR_RESPONSIBILITY_AREA,
        ERROR_START_TIME,
        ERROR_END_TIME,
        ERROR_SHUTDOWN_START_TIME,
        ERROR_SHUTDOWN_END_TIME,
        ERROR_EFFECT_BUSINESS_START_TIME,
        ERROR_EFFECT_BUSINESS_END_TIME,
        ERROR_SHUTDOWN_PERIOD,
        ERROR_EFFECT_BUSINESS_PERIOD,
        ERROR_PHENOMENON,
        ERROR_SHORTCUT_DESCRIPTION,
        ERROR_PROPERTY,
        ERROR_HAPPEN_DATE,
        ERROR_REASON,
        ERROR_INSPECTION,
        ERROR_CONSUME_BACKUP,
        ERROR_PROCESSORS,
        ERROR_TAKE_CHARGE,
        ERROR_CORRECTIVE_ACTION_AND_PREVENTION_MEASURES,
        REC_CREATE_TIME,
        REC_CREATOR,
        REC_REVISE_TIME,
        RECORD_REVISE_COUNT,
        REC_REVISOR,
    ):
        self.ERROR_REPORT_FILE_ID = ERROR_REPORT_FILE_ID
        self.ERROR_EQUIPMENT_NAME = ERROR_EQUIPMENT_NAME
        self.ERROR_RESPONSIBILITY_AREA = ERROR_RESPONSIBILITY_AREA
        self.ERROR_START_TIME = ERROR_START_TIME
        self.ERROR_END_TIME = ERROR_END_TIME
        self.ERROR_SHUTDOWN_START_TIME = ERROR_SHUTDOWN_START_TIME
        self.ERROR_SHUTDOWN_END_TIME = ERROR_SHUTDOWN_END_TIME
        self.ERROR_EFFECT_BUSINESS_START_TIME = ERROR_EFFECT_BUSINESS_START_TIME
        self.ERROR_EFFECT_BUSINESS_END_TIME = ERROR_EFFECT_BUSINESS_END_TIME
        self.ERROR_SHUTDOWN_PERIOD = ERROR_SHUTDOWN_PERIOD
        self.ERROR_EFFECT_BUSINESS_PERIOD = ERROR_EFFECT_BUSINESS_PERIOD
        self.ERROR_PHENOMENON = ERROR_PHENOMENON
        self.ERROR_SHORTCUT_DESCRIPTION = ERROR_SHORTCUT_DESCRIPTION
        self.ERROR_PROPERTY = ERROR_PROPERTY
        self.ERROR_HAPPEN_DATE = ERROR_HAPPEN_DATE
        self.ERROR_REASON = ERROR_REASON
        self.ERROR_INSPECTION = ERROR_INSPECTION
        self.ERROR_CONSUME_BACKUP = ERROR_CONSUME_BACKUP
        self.ERROR_PROCESSORS = ERROR_PROCESSORS
        self.ERROR_TAKE_CHARGE = ERROR_TAKE_CHARGE
        self.ERROR_CORRECTIVE_ACTION_AND_PREVENTION_MEASURES = (
            ERROR_CORRECTIVE_ACTION_AND_PREVENTION_MEASURES
        )
        self.REC_CREATE_TIME = REC_CREATE_TIME
        self.REC_CREATOR = REC_CREATOR
        self.REC_REVISE_TIME = REC_REVISE_TIME
        self.RECORD_REVISE_COUNT = RECORD_REVISE_COUNT
        self.REC_REVISOR = REC_REVISOR

    def __repr__(self) -> str:
        return f"dcyw0020(id={self.ERROR_REPORT_FILE_ID!r}, name={self.ERROR_EQUIPMENT_NAME!r}, fullname={self.ERROR_RESPONSIBILITY_AREA!r})"


def write_to_db():
    engine = create_engine(
        "mysql+pymysql://bwms:bwms_user@www.zjbaosight.com:3306/bwms?charset=utf8",
        echo=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    dcyw0020 = DCYW0020(
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        1.1,
        1.2,
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        0,
        "26",
    )
    session.add(dcyw0020)
    session.commit()
    session.close()

def read_from_db():
    engine = create_engine(
        "mysql+pymysql://bwms:bwms_user@www.zjbaosight.com:3306/bwms?charset=utf8",
        echo=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # 读取数据库
    a = session.query(DCYW0020).filter_by(ERROR_REPORT_FILE_ID="1B220231").first()
    print(a)
    session.close()


if __name__ == "__main__":
    write_to_db()
    # read_from_db()
    # print(ran
