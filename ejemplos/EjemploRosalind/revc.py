linea = raw_input()

def revcomp(linea):
    comp = ""
    for i in linea:
        if(i=="A"):comp += "T"
        elif(i=="C"):comp += "G"
        elif(i=="T"):comp += "A"
        elif(i=="G"):comp += "C"
    return comp[::-1]


print(revcomp(linea))
