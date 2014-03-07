def sed(pattern, replacemant, fail1, fail2):
    pattern = string
    replacemant = string
    fail1 = failname
    fail2 = failname
    try:
        fin = open(fail1, "r")
        fout = open(fail2, "w")
        for line in fin:
            line = line.replace(fail1, fail2)
            fount.write(line)
        fin.close()
        fout.close()
    except:
         print "Error!"      

