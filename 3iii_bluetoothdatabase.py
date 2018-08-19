import sqlite3 as lite
import sys
con = lite.connect('bluetoothdatabase.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS BLUETOOTH_data")
    cur.execute("CREATE TABLE BLUETOOTH_data(devicename TEXT, deviceaddress TEXT)")
