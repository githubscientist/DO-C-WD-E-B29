import shutil
import os
import time


class HealthMonitor:
    '''
        - The application runs indefinitely.

        - Check the drive usage
        - calculate the percentage of free space available

        - check if the free space percentage is less than 20
            - If yes, print an alert

        put the application to sleep for 1 minute (60 seconds)
    '''

    def __init__(self):
        self.total = 0
        self.used = 0
        self.free = 0

    def start(self):
        # Run the application indefinitely
        while True:
            # do the checks
            # get the drive usage
            self.total, self.used, self.free = shutil.disk_usage(os.getcwd())

            # the spaces are in bytes
            # convert them into GigaBytes
            totalGB = self.total / (2**30)
            usedGB = self.used / (2**30)
            freeGB = self.free / (2**30)

            # calculate the free percentage
            freePercentage = (freeGB / totalGB) * 100

            print('The system has a free percentage of about ',
                  freePercentage, '%', sep='')

            # check if we need to alert for less than 20%
            if freePercentage < 20:
                print('You are running on a low space')
            else:
                print('You have enough memory to manage applications')

            # put the application to go to sleep for 1 minute
            print('Putting the application to sleep for 10 seconds...')
            time.sleep(10)
