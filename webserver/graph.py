import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

def graph_data():
    # Connect to database
    db = '/home/pi/A01/database.db'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    style.use('fivethirtyeight')

    c.execute('SELECT timestamp, humidity FROM DATABASE_data')
    data = c.fetchall()

    timestamp = []
    humidity = []
   

    for row in data:
        humidity.append(row['humidity'])
        timestamp.append(parser.parse(row['timestamp']))
        

    plt.plot_date(humidity, '-')
    plt.savefig('/home/pi/WebService/templates/Index.html')
    c.close()
    conn.close()