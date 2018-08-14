#!/usr/bin/env python3
import time
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/A01/database.db'
sampleFreq = 1 # time in seconds

# get data from SenseHat sensor
def getDatabaseData():	
    sense = SenseHat()
    t = sense.get_temperature_from_humidity()
    h = sense.get_humidity()    
    t = round(t, 1)
    h =  round(h, 1)
    uploadData (t,h)

# log sensor data on database
def uploadData (t,h):	
    con=sqlite3.connect(dbname)
    curs=con.cursor()
    curs.execute("INSERT INTO DATABASE_data(timestamp, temp, humidity) values(datetime('now'), (?), (?))", (t,h))
    con.commit()
    con.close()
    
# display database data
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM DATABASE_data"):
        print (row)
    conn.close()

# main function
def main():
    for i in range (0,4):
        getDatabaseData()
        time.sleep(sampleFreq)
    displayData()

# Execute program 
main()