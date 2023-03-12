import cx_Oracle

connection = cx_Oracle.connect(user="xhadmin", password="bjtest",
                               dsn="10.70.86.2:1521/dbtestbj")
cursor = connection.cursor()

sql = """
SELECT * FROM xhcp.t_cpeg_apply_emp_list WHERE APPLY_NO = '180315'
"""

try:
    cursor.execute(sql)
    DataResult = cursor.fetchall()
    # print(DataResult)
    for row in DataResult:
        print(row, end="\n")
except Exception as e:
    print(e)
connection.commit()
connection.close()
