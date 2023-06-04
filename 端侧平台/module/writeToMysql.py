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

# print(sqlalchemy.__version__)

metadata_obj = MetaData()
engine = create_engine(
    "mysql+pymysql://admin:zhj123456@127.0.0.1:3306/test?charset=utf8"
)

test = Table(
    "py_test",
    metadata_obj,
    Column("id", String(10), primary_key=True),
    Column("reply", String(20), primary_key=True),
    Column("createtime", TIMESTAMP),
)

test2 = Table(
    "test2",
    metadata_obj,
    Column("id", String(10), ForeignKey("py_test.id")),
    Column("employee_dept", Integer, nullable=True),
)

# 打印metadata_obj 里面的表
for t in metadata_obj.sorted_tables:
    print("TableName:", t.name)

# 打印表中的column
for c in test.c:
    print("Column:", c)

# 打印表中的主键
for primary_key in test.primary_key:
    print("Primary Key:", primary_key)

# 打印表中的外键
for fkey in test2.foreign_keys:
    print("Fkey:", fkey)

# 打印表中的元数据
# 输出： metadata: MetaData()
# 输出： metadata: MetaData()
print("metadata:", test.metadata)
print("metadata:", test2.metadata)


print(test.c.id.name)
print(test.c.id.type)
print(test.c.id.nullable)
print(test.c.id.primary_key)
print(test2.c.id.primary_key)
print(test2.c.id.foreign_keys)

if test.c.id.table is test:
    print("True")

print(list(test2.c.id.foreign_keys)[0].column.table)

# with engine.connect() as conn:
#     # result = conn.execution_options(stream_results=True).execute(text("select * from py_test"))
#     # for i in result:
#     #     print(i)
#     conn.execute()


user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60), key="email"),
    Column("nickname", String(50), nullable=False),
)

user_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_value", String(100)),
)

metadata_obj.create_all(engine)
