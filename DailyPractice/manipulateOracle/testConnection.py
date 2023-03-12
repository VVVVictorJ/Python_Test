import cx_Oracle

connection = cx_Oracle.connect(user="bjapp", password="bjap2014",
                               dsn="10.70.36.2:15002/dbprodbj")
cursor = connection.cursor()

contract_no = "BGS1801"

sql = """SELECT * FROM XHCP.T_CPEG_EMP_ASSIGNATION WHERE CONTRACT_NO = :cn
"""

cursor.execute(sql, cn=contract_no)

for row in cursor:
    print(row[0], row[1])
