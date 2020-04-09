from test_creation_grille_alea import grille
from création_dimacs import crea_dimacs
from créa_cnf import crea_cnf

grille=grille()
(cnf,clauses)=crea_cnf(grille)
crea_dimacs(clauses,cnf)