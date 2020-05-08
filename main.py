from test_creation_grille_alea import grille
from creation_dimacs import crea_dimacs
from crea_cnf import crea_cnf
import os
#import sys

#grille=open(sys.argv[1], "r")
#taille=int(sys.argv[2])
(grille,taille)=grille()
(clauses,var,cnf)=crea_cnf(grille,taille)
crea_dimacs(clauses,var,cnf,taille)
os.system('./cryptominisat5-amd64-linux Dimacs.cnf dimacs.txt')

#grille.close()
