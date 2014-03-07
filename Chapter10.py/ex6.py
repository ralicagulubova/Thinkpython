def has_duplicate(list):
    new_list = list [:]
    new_list.sort()
    for i in range(len(new_list) - 1):
        if new_list[i] == new_list[i+1]:
            print True
        elif new_list[i] != new_list[i+1]:
            print False
            
            
has_duplicate([1, 3, 2, 6, 8, 2])