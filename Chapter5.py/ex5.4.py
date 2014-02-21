a = input("Please enter a number greather then 0 for 'a' ")
b = input("Please enter a number greather then 0 for 'b' ")
c = input("Please enter a number greather then 0 for 'c' ")
def is_triangle():
    if a + b ==c and c + a == b and b + c == a:
        print "yes"
    if     a + b > c and c + a > b and b + c > a:
        print "no"
        
is_triangle()
        
        
  
        