def nested_sum(nestedlist, newlist = [0]):
    def flatlist(nestedlist):
        for i in range(len(nestedlist)):
            if type(nestedlist[i]) == int:
                    newlist.append(nestedlist[i])
            else:
                    flatlist(nestedlist[i])
        return newlist
    
    flatlist(nestedlist)
    print sum(newlist)   
        
nested_sum([[2, 5, 8], [3, 8, 9], [2, 6, 8]])           
    

    