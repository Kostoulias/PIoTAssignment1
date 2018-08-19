#!/usr/bin/env python3
import os
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from datetime import datetime
from flask import Flask, render_template, request
from sense_hat import SenseHat


dbname='/home/pi/A01/database.db'



def getData():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    c = curs.execute('SELECT (timestamp, humidity) from DATABASE_data')
    data = curs.fetchall()
    
    timestamp = []
    humidity = []

    for row in data:
        humidity.append(row['humidity'])
        timesstamp.append(parser.parse(row['timestamp'])
    
    
    c.close()
    conn.close()

def graph():
    # graph code
    plt.plot(timestamp, humidity)
    plt.grid()
    plt.title("Humidity over Time")
    plt.xlabel("Hour (in AEST)")
    plt.ylabel("Humidity in %")
    plt.show()
    
getData()