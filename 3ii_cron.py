#!/usr/bin/env python3
from crontab import CronTab
    
#Init cron
cron = CronTab(user='pi')

#Add new cron job
job  = cron.new(command='/home/pi/A01/3ii_pushbullet.py')

#Job settings set to run every hour
job.hour.every(1)
cron.write()
