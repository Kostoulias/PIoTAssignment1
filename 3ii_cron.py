#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')

#add new cron job
job  = cron.new(command='/home/pi/A01/3ii_pushbullet.py')

#job settings set to run every hour
job.hour.every(1)
cron.write()
