def is_power(a, b):
    if a == b or a ==1:
        return True
    elif a % b !=0 or a == 0:
        return False
    else:
        return is_power(a / b, b)
    
    
    is_powder(4,6)
    