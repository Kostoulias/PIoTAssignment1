#!/usr/bin/env python3
import time
import pytz
import datetime
import sqlite3
import os
from sense_hat import SenseHat
dbname='/home/pi/A01/database.db'
sampleFreq = 1 # time in seconds



dt_utcnow = datetime.datetime.now(tz=pytz.UTC) #UTC Timezone
dt_aest = dt_utcnow.astimezone(pytz.timezone('Australia/Melbourne')) #Melbourne Timezone


# get data from SenseHat sensor
def getDatabaseData():	
    sense = SenseHat()
    t = sense.get_temperature()
    t_corr = t - 21
    h = sense.get_humidity()    
    t_corr = round(t_corr, 1)
    h =  round(h, 1)
    uploadData (t_corr,h)

# log sensor data on database
def uploadData (t_corr,h):	
    now = dt_utcnow.astimezone(pytz.timezone('Australia/Melbourne'))
    dt = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    con=sqlite3.connect(dbname)
    curs=con.cursor()
    curs.execute("INSERT INTO DATABASE_data(timestamp, temp, humidity) values((?), (?), (?))", (dt,t_corr,h))
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