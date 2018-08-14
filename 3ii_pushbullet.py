#!/usr/bin/env python3
import requests
import json
import os

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()



#Access token is unique to account. Replace with your own on Pushbullet website
JAMES_ACCESS_TOKEN="o.jzjUdnNHMOeAr5wZVJ3m8uxNMcencmMr"
KHOA_ACCESS_TOKEN="" #Fill Access Token here 
def send_notification_via_pushbulletjames(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + JAMES_ACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('Complete sending')

def send_notification_via_pushbulletkhoa(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + KHOA_ACCESS_TOKEN,  
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('Complete sending')
       

#main function
#reads the temperature and if temp is 20 degrees or under send message via pushbullet
#if over 20 degrees then display current temp reading to sense hat
def main():
    temp = sense.get_temperature()
    if temp <= 20:
        send_notification_via_pushbulletjames("3ii Notification", "It's cold! Bring a sweater.")
        #send_notification_via_pushbulletkhoa("3ii Notification", "It's cold! Bring a sweater.")
    else:  
        sense.show_message('Temp: {0:0.1f} *c'.format(temp), scroll_speed=0.05)
        sense.clear()
#Execute main
main()
