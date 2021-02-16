import datetime
import winsound
alarm_hour = int(input("What hour do you want ot wake up?"))
alarm_minute = int(input("What minute do you want ot wake up?"))
am_pm = str(input("pm or am?"))

if am_pm == "pm":
    alarm_hour = alarm_hour + 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
        print("Wake up")
        winsound.PlaySound("Music", winsound.SND_FILENAME)
        break
print("exit")
