import time
from sched import scheduler
import winsound as ws

alarm_time = input('Enter target time:')

def set_alarm(alarm_time,sound,message):
    s = scheduler(time.time,time.sleep)
    s.enterabs(alarm_time,1,print,argument=(message))
    s.enterabs(alarm_time,1,ws.PlaySound,argument=(sound,ws.SND_FILENAME))
    print(f'Alarm set for {time.asctime(time.localtime(alarm_time))}')
    s.run()