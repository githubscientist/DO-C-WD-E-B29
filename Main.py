# Unit test for HealthMonitor.py

# import the class from the module HealthMonitor
from HealthMonitor import HealthMonitor


def main():
    '''
        This function is the entry point
    '''
    # create an object to the class
    healthMonitor = HealthMonitor()
    healthMonitor.start()


# boiler plate for main
if __name__ == "__main__":
    main()
