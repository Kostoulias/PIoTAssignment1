import sqlite3 as lite
import sys
#Connect to database file
con = lite.connect('database.db')
#Drops table if it exists and create a database with the following attributes
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS DATABASE_data")
    cur.execute("CREATE TABLE DATABASE_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
