class Time(object):
    pass

time = Time()
time.hour = 11
time.minute = 59
time.second = 30
time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30

def is_after(time, time1):
    print (time.hour, time.minute,time.second ) > (time1.hour, time1.minute, time1.second)
    
    
is_after(time, time1)
    
    

     
