list = [1, 3, 5, 4, 8, 9]
def chop(list):
    del list[0]
    del list[-1]
chop(list)
print list


