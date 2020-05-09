##INIT TKINTER

import numpy as np
import random


#the function list_possible() allows to differentiate the boxes, for an angle the box will contain the numbers from 1 to 4 and empty
# for a side from 1 to 6 and empty #
#cases "central" 0 to 9 and empty
#empty 0 or 1 if the grid is on side 1

#For example, an angle is surrounded by only 4 squares (3+itself) etc...

def list_possible(i,j,nb):
    nb_cotes = 0
    if i == 0 : nb_cotes=nb_cotes+1
    if j == 0 : nb_cotes=nb_cotes+1
    if i == nb-1 : nb_cotes=nb_cotes+1
    if j == nb-1 : nb_cotes=nb_cotes+1

#there are many more gaps than numbers so that the grid remains solvent enough.
#in fact each cell will then take a value from the list that corresponds to it.
    return {
        0 : [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',0,1,2,3,4,5,6,7,8,9],
        1 : [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',0,1,2,3,4,5,6],
        2 : [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',0,1,2,3,4],
        4 : [' ',0,1]
    }[nb_cotes]

def grille():

    NB_DE_CASES_MAX=10

    nbr_cases_possible=[]
    for i in range(1,NB_DE_CASES_MAX+1):
        nbr_cases_possible.insert(i,i)

    NB_DE_CASES=random.choice(nbr_cases_possible)

    #NB_DE_CASES=7

# Displaying numbers in the grid
# thanks to the fct list_possible explained above, each box is assigned a random or empty number.
# the grid is in the form of a matrix, list of list, each list corresponds to a line

    grille3=np.array([[random.choice(list_possible(i,j,NB_DE_CASES)) for j in range(NB_DE_CASES)] for i in range(NB_DE_CASES)])

#The grid is obviously displayed in the console so that the user can see it.
    print (grille3)

    taille=NB_DE_CASES

    return (grille3,taille)