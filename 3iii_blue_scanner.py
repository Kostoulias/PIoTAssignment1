#!/usr/bin/env python3
import bluetooth
import os
import time
import sqlite3
from sense_hat import SenseHat
dbname = '/home/pi/A01/bluetoothdatabase.db'

# Main function
def main():
    #Pi will search for detectable bluetooth devices and their device names
    nearby_devices = bluetooth.discover_devices(lookup_names = True)
    #Will run loops based on the amount of devices it finds
    for mac_address, name in nearby_devices:
        device_address = mac_address
        device_name = name
        #Access database and see if it matches any of the currently discoverable devices, else insert the new devices into database
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        curs.fetchone()
        curs.execute("SELECT * FROM BLUETOOTH_data WHERE devicename= ? AND deviceaddress= ?", (device_name, device_address,))
        found = curs.fetchone()
        if found:
            displayGreetings(device_name, device_address)
        else:
            insertDevice(device_name, device_address)

def displayGreetings(device_name, device_address):
    #Grabs current date and time and formats into readable format.
    dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
    print("\nCurrently: {}".format(dt))
    time.sleep(3) #Sleeps three seconds 
    #Grabs information from database to display message and information of device.
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("SELECT * FROM BLUETOOTH_data WHERE deviceaddress= ?", (device_address,))
    print("Hello! Your device ({}) has the MAC address: {}".format(device_name, device_address))
    sense = SenseHat()
    temp = round(sense.get_temperature(), 1)
    sense.show_message("Hi {}! Current Temp is {}*c".format(device_name, temp), scroll_speed=0.05)
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    #Optional: Prints entire database content to show registered devices
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM BLUETOOTH_data"):
        print (row)
    conn.close()

def insertDevice(device_name, device_address):
    #Insert new device information into database and then run function to display greeting.
    print("\nThe following device information will be inserted into the database:\n {} {}".format(device_name, device_address))
    con=sqlite3.connect(dbname)
    curs=con.cursor()
    curs.execute("INSERT INTO BLUETOOTH_data(devicename, deviceaddress) values((?), (?))", (device_name, device_address))
    con.commit()
    con.close()
    displayGreetings(device_name, device_address)

main()
