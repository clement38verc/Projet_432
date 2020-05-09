from test_creation_grille_alea import grille
from creation_dimacs import crea_dimacs
from crea_cnf import crea_cnf
from solution import resolution_grille
import numpy as np
import os

#Ask if the user want use our generator or his/her grid
rep=input("Which grid do you want to use? (generator or personal)\n")
if rep[0]=="g":
    #call the generator to create a grid
    (grille,taille)=grille()
elif rep[0]=="p":
    #explain the format of a grid
    print("The format of the grid is .txt file with a grid. Each cell in the same ligne is separated by a tabulation (like in the exemple grille.txt)\n")
    gn=input("What is your grid ?\n")
    #extract the grid and transform it in a np.array
    grille = np.loadtxt(gn,delimiter="\t",dtype=str)
    #Ask the size of the grid
    t=input("How wide is it ?\n")
    taille=int(t)
else: #Error if not generator or personal
    raise ValueError("it is not generator or personal\n")

#create cnf of the grid
(clauses,var,cnf)=crea_cnf(grille,taille)
#create Dimacs.cnf
crea_dimacs(clauses,var,cnf,taille)
#Save the result of sat-solver for Dimacs.cnf in dimas.txt
os.system('./cryptominisat5-amd64-linux Dimacs.cnf>dimacs.txt')
#print the result
resolution_grille(taille,grille)

