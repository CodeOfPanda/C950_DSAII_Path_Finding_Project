class Truck:
    # deliveries start at 8 am and are finished when all the packages (40) are delivered.
    # time needs to be tracked (at least polonomial time or better but does not need to be optimized...)
    # one driver per truck
    # max of 16 packages per truck at one time. (can return to refill)
    # avg speed of 18 mph
    
    
    # constructor method
    def __init__(self, start_time='8:00', size=16):
        self.time = start_time
        self.speed = 18
        self.packages = []  # should be the package id's being passed in i think.
        for i in range(size):
            self.packages.append([])
        
    def get_time(self):
        return self.time()  # need to look into time tracking methods in python (datetime, time())
               
    def set_time(self, time):
        self.time = time
        