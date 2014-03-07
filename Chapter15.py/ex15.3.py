import copy

class Rectangle(object):
    pass

class Point(object):
    pass

box = Rectangle()
box.wight = 3.0
box.heigth = 2.0
box.corner = Point()
box.corner.x = 5.0
box.corner.y = 1.0
print box.corner.x, box.corner.y


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    
    print rect.corner.x, rect.corner.y
    
    
def move_rectangle_copy(rect, dx, dy):
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new


move_rectangle_copy(box, 12, 12)
