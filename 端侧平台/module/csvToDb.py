import pandas as pd
from sqlalchemy import create_engine
from processDocx import ProcessDocx
import sqlalchemy

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

obj = ProcessDocx()
df = pd.DataFrame(
    obj.processDocxTableInfo(
        filepath=f"E:\\code\\python\\Python_Test\\端侧平台\\module\\src\\2518_20220110_湛江钢铁_炼钢热轧L3系统_故障报告书_B.docx",
    )
)

df.to_sql(
    "errorProcessTableMessage",
    con=engine,
    chunksize=10000,
    if_exists="replace",
    index=False,
)
