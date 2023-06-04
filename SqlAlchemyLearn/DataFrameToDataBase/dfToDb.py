import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.types import DATE, CHAR, VARCHAR

# data = pd.DataFrame(np.random.rand(4,4), index=list('abcd'),columns=['col_1', 'col_2','col_3','col_4'])

engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

# DTYPES = {''}

data = pd.DataFrame(
    np.random.randint(1, 100, size=(4, 4)),
    index=list("abcd"),
    columns=["col_1", "col_2", "col_3", "col_4"],
)
print(data)

data.to_sql(
    "dftest",
    con=engine,
    chunksize=10000,
    if_exists="replace",
    index=False
)
