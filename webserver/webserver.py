#!/usr/bin/env python3
import os
import sqlite3
import matplotlib.pylot as plt
from datetime import datetime
from flask import Flask, render_template, request
from sense_hat import SenseHat

app = Flask(__name__)
dbname='/home/pi/A01/database.db'



plt.ion()
x = []
y = []

query = """
        select (timestamp, humidity), 
        from DATABASE_data
        """

def getData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()


def graph():
    # graph code
    plt.plot(timestamp, humidity)
    # set the X ticks every 2 hours
    plt.xticks(range(0, 23, 2))
    # draw a grid
    plt.grid()
    # set title, X/Y labels
    plt.title("Humidity over Time")
    plt.xlabel("Hour (in AEST)")
    plt.ylabel("Humidity (in %)")

@app.route("/")
def index():
    timestamp, humidity = graph()
    templateData = {
        'time': timestamp,
        'temp': humidity
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
