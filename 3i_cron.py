#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')


#add new cron job
job  = cron.new(command='/home/pi/A01/3idemo.py')

#job settings to run every minute (currently for testing purposes)
job.minute.every(30)
cron.write()
