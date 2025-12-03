import datetime
import time

while True:
    time.sleep(1)
    currentTime = datetime.datetime.now().strftime('%H:%M:%S')
    print(currentTime)
