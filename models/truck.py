class Truck:
    # deliveries start at 8 am and are finished when all the packages (40) are delivered.
    # time needs to be tracked (at least polonomial time or better but does not need to be optimized...)
    # one driver per truck
    # max of 16 packages per truck at one time. (can return to refill)
    # avg speed of 18 mph

    # T2 (leaves at 8:00am): packages will contain id's: [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
    # T1 (leaves at 9:05am): packages will contain id's: [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
    # T3 (leaves ~ 10:20am): packages will contain id's [5, 9, 2, 4, 7, 8, 10, 11]

    # constructor method
    def __init__(self, start_time='8:00'):
        self.time = start_time
        self.speed = 18
        self.packages = []

    def load_packages(self, package):
        self.packages.append(package)
        
    def get_packages(self):
        return self.packages

    def print(self):
        for package in self.packages:
            print(package.p_id)
