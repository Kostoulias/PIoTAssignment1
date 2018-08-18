#!/usr/bin/env python3
import bluetooth
import os
import time
import sqlite3
from sense_hat import SenseHat
dbname = '/home/pi/A01/bluetoothdatabase.db'

# Main function
def main():
    user_name = input("Enter your name: ")
    device_name = input("Enter the name of your phone: ")
    search(user_name, device_name)

# Search for device based on device's name
def search(user_name, device_name):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        if SELECT deviceadress FROM BLUETOOTH == device_address


        for mac_address in nearby_devices:
            if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                device_address = mac_address
                con=sqlite3.connect(dbname)
                curs=con.cursor()
                curs.execute("INSERT INTO BLUETOOTH_data(username, devicename, deviceaddress) values((?), (?), (?))", (user_name, device_name, device_address))
                con.commit()
                con.close()
                break
        if device_address is not None:
            print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
            sense = SenseHat()
            temp = round(sense.get_temperature(), 1)
            sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
            conn=sqlite3.connect(dbname)
            curs=conn.cursor()
            print ("\nEntire database contents:\n")
            for row in curs.execute("SELECT * FROM BLUETOOTH_data"):
                print (row)
            conn.close()
        else:
            print("Could not find target device nearby...")

#Execute program
main()
