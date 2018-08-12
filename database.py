import sqlite3 as lite
import sys
con = lite.connect('database.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS DATABASE_data")
    cur.execute("CREATE TABLE DATABASE_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
