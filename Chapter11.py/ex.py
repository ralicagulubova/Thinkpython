dictionary = dict()
fin = open ("word.txt")
line = fin.readline()
def dictionary_word():
    index = 0
    while index <= 1000 :
        word = line.strip()
        dictionary[word] = index
        index += 1 
    return dictionary   
    
