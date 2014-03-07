import math
class Point(object):
    pass
    
def distance_between(p1, p2):
    dy = p2.y - p1.y
    dx = p2.x - p2.x
    distance = math.sqrt(dy**2 + dx**2)
    print distance
    
p1 = Point()
p2 = Point()
    
p1.x = 3.0
p2.x = 4.0
p1.y = 1.0
p2.y = 4.0
   

    
distance_between(p1,p2)    
