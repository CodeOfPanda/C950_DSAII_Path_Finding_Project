import datetime

class Truck:
    # T2 (leaves at 8:00am): packages will contain id's: [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
    # T1 (leaves at 9:05am): packages will contain id's: [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
    # T3 (leaves ~ 10:20am): packages will contain id's [5, 9, 2, 4, 7, 8, 10, 11]

    # constructor method
    def __init__(self, hour, minute, second, name):
        self.name = name
        self.speed = 18
        self.distance = 0.0
        self.leave_time = datetime.time(hour, minute, second, 0)
        self.end_time = datetime.time(hour, minute, second, 0)
        self.packages = []


    # adds id's to package array.
    def load_packages(self, package):
        self.packages.append(package)
     
    # returns package array   
    def get_packages(self):
        return self.packages
    
    def get_distance(self):
        return self.distance
    
    def set_distance(self, new_distance):
        self.distance = new_distance
            
    def get_leave_time(self):
        return self.leave_time
    
    def set_end_time(self, end_time):
        self.end_time = end_time
        
    def get_end_time(self):
        return self.end_time

    def calculate_time(self, distance):
        seconds = float(distance) / 0.005 #0.005 is miles per second at 18mph
        return seconds
