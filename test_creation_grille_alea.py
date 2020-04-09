# A MODIFIER
##### ICI JE CREER DEUX GRILLES, LA PREMIERE AVEC DES VALEURS ALEATOIRES PAS FORCEMENT RESOLVABLE MAIS COHERENTE ET LAUTRE QUE DES 1 #####




##INIT TKINTER

import numpy as np
import random
from tkinter import *
from math import sqrt

def list_possible(i,j,nb):
    nb_cotes = 0
    if i == 0 : nb_cotes=nb_cotes+1
    if j == 0 : nb_cotes=nb_cotes+1
    if i == nb-1 : nb_cotes=nb_cotes+1
    if j == nb-1 : nb_cotes=nb_cotes+1

    return {
        0 : [' ',' ',' ',' ',' ',0,1,2,3,4,5,6,7,8,9],
        1 : [' ',' ',' ',' ',' ',0,1,2,3,4,5,6],
        2 : [' ',' ',' ',' ',' ',0,1,2,3,4],
        4 : [' ',' ',' ',' ',' ',0,1]
    }[nb_cotes]

def grille():
    fen=Tk()
    COTE=750
    MARGE=0
    DECALAGE=20
    can=Canvas(fen,bg="light gray", height=(COTE+MARGE), width=2*(MARGE+COTE)+DECALAGE)
    can.pack()

    NB_DE_CASES_MAX=80

    nbr_cases_possible=[]
    for i in range(1,NB_DE_CASES_MAX+1):
        nbr_cases_possible.insert(i,i)

    print (nbr_cases_possible)

#NB_DE_CASES=random.choice(nbr_cases_possible)
    NB_DE_CASES=15

    print (NB_DE_CASES)

    PAS= COTE/NB_DE_CASES

#INIT GRILLE DEPART
    x=0
    while (x<=NB_DE_CASES):
        can.create_line(0,PAS*x,COTE,PAS*x,fill='black')
        x=x+1

    y=0
    while (y<=NB_DE_CASES):
        can.create_line(PAS*y,0,PAS*y,COTE,fill='black')
        y=y+1

    can.create_rectangle(1.5,1.5,COTE,COTE)



#creation du centre de la grille
grille3=np.array([[random.choice(list_possible(i,j,NB_DE_CASES)) for j in range(NB_DE_CASES)] for i in range(NB_DE_CASES)])
print (grille3)
for i in range (NB_DE_CASES):
    for j in range (NB_DE_CASES):


    grille3=np.array([[random.choice(list_possible(i,j,NB_DE_CASES)) for j in range(NB_DE_CASES)] for i in range(NB_DE_CASES)])
    print (grille3)
    for i in range (NB_DE_CASES):
        for j in range (NB_DE_CASES):


        can.create_text(((PAS)/2)+((PAS)*i),(((PAS)/2)+(PAS)*j),text=grille3[j][i])
can.create_rectangle(1.5,1.5,COTE,COTE)


            can.create_text(((PAS)/2)+((PAS)*i),(((PAS)/2)+(PAS)*j),text=grille3[j][i])
    can.create_rectangle(1.5,1.5,COTE,COTE)


#INIT GRILLE FIN


    a=0
    while (a<=NB_DE_CASES):
        can.create_line(COTE+DECALAGE,PAS*a,DECALAGE+(COTE*2),PAS*a,fill='black')
        a=a+1

    b=0
    while (b<=NB_DE_CASES):
        can.create_line(PAS*b +DECALAGE+COTE,0,PAS*b+DECALAGE+COTE,COTE,fill='black')
        b=b+1



    grille=[[0 for t in range(NB_DE_CASES)] for v in range(NB_DE_CASES)]
    grille4=[[0 for t in range(NB_DE_CASES)] for v in range(NB_DE_CASES)]




    for c in range (NB_DE_CASES):
        for l in range (NB_DE_CASES):
            can.create_text(((PAS)/2)+((PAS)*c)+COTE+DECALAGE,(((PAS)/2)+((PAS)*l)),text=grille[c][l])
            if grille3[c][l]==9:
                for a in range (c-1,c+2):
                    for b in range (l-1,l+2):
                        grille4[a][b]=1
                        #print(c,l)


#PB DE COORDONER SI C SUR LES COTER OU ANGLE
#        if grille3[c][l]==0:
 #           for a in range (c-1,c+2):
  #              for b in range (l-1,l+2):
   #                 grille4[a][b]=0
    #                print(c,l)



    for c in range (NB_DE_CASES):
        for l in range (NB_DE_CASES):
            if grille4[c][l]==1:
                    can.create_rectangle(PAS*c+DECALAGE+COTE,PAS*l,PAS*c+DECALAGE+COTE+PAS,PAS*l+PAS,fill='black')
            else :
                    can.create_rectangle(PAS*c+DECALAGE+COTE,PAS*l,PAS*c+DECALAGE+COTE+PAS,PAS*l+PAS,fill='white')

    can.create_rectangle((COTE + DECALAGE),1.5,2*(MARGE+COTE)+DECALAGE,COTE)


    fen.mainloop()

    return grille3


