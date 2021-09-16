from pynotifier import Notification
import psutil

psutil.cpu_times()
disk = psutil.disk_usage(".")
battery = psutil.sensors_battery()

Notification(
    title='Your disk Storage / Battery',
    description=str(disk.total)+' mb,'+str(battery.percent)+'% ',
    # On Windows .ico is required, on Linux -.png
    icon_path='/absolute/path/to/image/icon.png',
    duration=5,                                   # Duration in seconds
    urgency='normal'
).send()
