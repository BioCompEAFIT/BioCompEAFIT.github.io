entrada = raw_input()

lalista = []
mydict = {"A":0, "C":0, "T":0, "G":0}

for elemento in entrada:
    if elemento == "A":
        mydict["A"]+=1
    elif elemento == "C":
        mydict["C"]+=1
    elif elemento == "T":
        mydict["T"]+=1
    elif elemento == "G":
        mydict["G"]+=1

print("%d %d %d %d"% (mydict["G"], mydict["A"], mydict["C"], mydict["T"]))
#print mydict.values()
