import os

def crea_dimacs(nbclaus,nbvar,cnf,taille):
    #create or erase the last Dimacs.cnf
    d=open("Dimacs.cnf", "w")
    #write the first line of a Dimacs
    d.write("p cnf "+str(nbvar)+" "+str(nbclaus)+"\n")
    #number of variables in the grid
    k=taille**2
    f=0
    #cl=a cell of the grid
    for cl in cnf:
        #add the max of n when we finished with a cell to pass to the next cell
        k+=f
        f=0
        #dico=one clause
        for dico in cl:
            #key=variable in a clause
            for key in dico.keys():
                #if the size of a key is 2, we have a variable of the grid
                if (len(key)==2):
                    (i,j)=key
                    #write the value corresponding to the position of the variable in the grid with - if it is false
                    if (dico[key]==True):
                        d.write(str(i*taille+j+1)+" ")
                    else :
                        d.write("-"+str(i*taille+j+1)+" ")
                #if the size of a key is 3, we have one possibility for the solution
                else:
                    (i,j,n)=key
                    #We take the max of n without change k
                    if (f<n):
                        f=n
                    #write with the number corresponding to the size of the grid add number of cases in the last cell add the actual case number
                    if (dico[key]==True):
                        d.write(str(k+n)+" ")
                    else :
                        d.write("-"+str(k+n)+" ")
            d.write("0\n")
    d.close()