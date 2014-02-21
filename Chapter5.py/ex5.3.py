a = input("Please enter a  number for 'a'")
b = input("Please enter a number for 'b'")
c = input("Please enter a number for 'c'")
n = input("Please enter a number for 'n'")
def chek_fermat():
    if a**n + b**n == c**n and n>2:
        print " Fermat was wrong"
    else:
        print  "Fermat was rigth"       
        
        
chek_fermat()