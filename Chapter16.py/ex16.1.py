class Time(object):
    pass

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time):
    
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)
    

    
print_time(time)
