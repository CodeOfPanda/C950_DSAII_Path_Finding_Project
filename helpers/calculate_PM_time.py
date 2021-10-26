import datetime

def get_PM_time(user_in):
    #Create a datetime.time variable out of the string input time
    input_time = datetime.datetime.strptime(user_in, '%H:%M').time()
    #create a dummy datetime variable for noon comparison below
    noon = datetime.datetime.now()
    #set the time to 11:59:59:59
    noon = noon.replace(hour=11, minute=59, second=59, microsecond=59)
    if input_time > noon.time():
        return input_time
    else:
        #Create a datetime.datetime variable for the current day's calendar day with the input_time as the time, and then increment it 12 hours
        #This converts 12 hour time to 24 hour time for correct PM values 
        new_input_time = datetime.datetime.combine(datetime.date.today(), input_time) + datetime.timedelta(hours=12)
        #return just the time portion of the datetime variable
        return new_input_time.time()
    