from test_creation_grille_alea import grille
from création_dimacs import crea_dimacs
from créa_cnf import crea_cnf

(grille,taille)=grille()
(clauses,var,cnf)=crea_cnf(grille,taille)
crea_dimacs(clauses,var,cnf,taille)
