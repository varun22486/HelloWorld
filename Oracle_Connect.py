import cx_Oracle
db_name=localhost
port=1521
service=orcl
dsn=cx_Oracle.makedsn(db_name,port,service_name=service)
con=cx_Oracle.connect(sys,orcl,dsn)
cursor = con.cursor()
cursor.execute("select *  from SYSTEM.user_details")
rows=cursor.fetchall()
for line in rows:
    print(line)
print("Total number of rows in table are %s" % len(rows))
print("Oracle Version is " + cx_Oracle.version + " and connection version is " + con.version)
cursor.close()
con.close()