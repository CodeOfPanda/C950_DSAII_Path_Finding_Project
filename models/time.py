import datetime

class Time:
    def __init__(self, hour, minute, second):
        self.date = datetime.datetime.now()
        self.time = self.date.replace(hour=hour, minute=minute, second=second, microsecond=0)
        
    def get_time(self):
        return self.time.time()
    
    def set_time(self, seconds):
        self.time = self.time + datetime.timedelta(seconds=seconds)