#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connection(host="localhost",user="root",passwrd="",db="hbtn_0e_0_usa",port=3306)
cur=db.cursor
cur.execute("SELECT * FROM states")
rows=cur.fetchall()
for row in rows:
   print(row)
cur.close()
db.close()
