import sqlite3 as lite
import sys
con = lite.connect('database.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS database_data")
    cur.execute("CREATE TABLE database_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
