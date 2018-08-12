from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/pi/A01/3idemo.py')

#job settings to run every minute (currently for testing purposes)
job.minute.every(1)
cron.write()
