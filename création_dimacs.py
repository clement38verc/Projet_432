import os
def crea_dimacs(nbclaus,c):
    d=open("Dimacs.cnf", "w")
    d.write("p cnf 9 "+str(nbclaus)+"\n")
    for el in c:
        if (el == "."):
            d.write(" 0\n")
        if (el=="+"):
            d.write(" ")
        if (el=="a"):
            d.write("1")
        if (el=="b"):
            d.write("2")
        if (el=="c"):
            d.write("3")
        if (el=="d"):
            d.write("4")
        if (el=="e"):
            d.write("5")
        if (el=="f"):
            d.write("6")
        if (el=="g"):
            d.write("7")
        if (el=="h"):
            d.write("8")
        if (el=="i"):
            d.write("9")
        if (el=="-"):
            d.write(el)
    d.write(" 0")
    d.close()