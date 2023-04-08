import psycopg2

#conn = psycopg2.connect(database="postgres",
#                        user="postgres",
#                        password="123456",
#                        host="127.0.0.1",
#                        port="5432")
conn = psycopg2.connect(database="myDatabase",
                        user="vic",
                        password="123456",
                        host="127.0.0.1",   
                        port="5432")

print('postgreSQL数据库"postgres"连接成功!')

cursor = conn.cursor()

#cursor.execute("SELECT deptid, deptname, createtime FROM department")    

#rows = cursor.fetchall()

#for row in rows:
#    print(row[0], row[1], row[2])

conn.close()

