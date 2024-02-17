#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connection(host="localhost",user=sys.argv[1],passwrd=sys.argv[2],db=sys.argv[3],port=3306)
cur=db.cursor
cur.execute("SELECT * FROM states")
rows=cur.fetchall()
for row in rows:
   print(row)
cur.close()
db.close()
