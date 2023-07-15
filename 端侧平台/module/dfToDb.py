import pandas as pd
import sqlalchemy
from processDocx import ProcessDocx
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

obj = ProcessDocx()
df = pd.DataFrame(
    obj.processDocxTableInfo(
        filepath=f"E:\\code\\Python\\端侧平台\\src\\20220325_湛江钢铁_物质出入厂系统_故障报告书_B(1).docx",
    )
)

df.to_sql(
    "errorProcessTableMessage",
    con=engine,
    chunksize=10000,
    if_exists="replace",
    index=False,
)
