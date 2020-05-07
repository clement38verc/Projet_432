import os

def crea_dimacs(nbclaus,nbvar,cnf,taille):
    d=open("Dimacs.cnf", "w")
    d.write("p cnf "+str(nbvar)+" "+str(nbclaus)+"\n")
    k=taille**2
    f=0
    for cl in cnf:
        k+=f
        f=0
        for dico in cl:
            for key in dico.keys():
                if (len(key)==2):
                    (i,j)=key
                    if (dico[key]==True):
                        d.write(str(i*taille+j+1)+" ")
                    else :
                        d.write("-"+str(i*taille+j+1)+" ")
                else:
                    (i,j,n)=key
                    if (f<n):
                        f=n
                    if (dico[key]==True):
                        d.write(str(k+n)+" ")
                    else :
                        d.write("-"+str(k+n)+" ")
            d.write("0\n")
    d.close()