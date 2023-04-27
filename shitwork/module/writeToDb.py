import psycopg2
import pandas as pd 
from io import StringIO

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
try:
    df = pd.read_csv('test.csv')

    output = StringIO()

    df.to_csv(output, sep='\t',index=False,header=False)
    
    output1 = output.getvalue()
    
    cursor = conn.cursor()
    
    cursor.execute("set search_path='public';")
    
    cursor.copy_from(StringIO(output1), "docxinfo")
    #
    conn.commit()
#cursor.execute("select * from pg_tables where schemaname = 'public';")
#data = cursor.fetchall()
#data = pd.read_sql(r"select * from pg_tables where schemaname = 'public';",
#                   con=conn)
#print(data.head())
    cursor.close()























#print(df)
#cursor.execute("SELECT deptid, deptname, createtime FROM department")    

#rows = cursor.fetchall()

#for row in rows:
#    print(row[0], row[1], row[2])

finally:
    conn.close()

