import numpy
from itertools import combinations

#Management of a basic cell
def cas_normal(i,j,n,nbcl,var):
    #list of clauses(=dictionnary)
    res=[]
    jus=dict()
    #a list to calculate the number of different solutions
    nbc=[]
    c=1
    cases = [(i,  j), (i+1,  j), (i-1,  j), (i,  j+1),(i+1,  j+1), (i-1,  j+1), (i,  j-1), (i+1,  j-1), (i-1,  j-1)]
    #create the clauses corresponding to "one case implies one solution"
    for k in combinations(cases,n):
        for p in cases:
            cas=dict()
            if (p in k):
                cas[p]=True
            else:
                cas[p]=False
            cas[(i,j,c)]=False
            nbcl+=1
            res.append(cas)
        c+=1
    c-=1
    o=1
    #create the clause corresponding to "at least one case is true"
    while (o<=c):
        jus[(i,j,o)]=True
        nbc.append((i,j,o))
        o+=1
    nbcl+=1
    res.append(jus)
    var+=len(nbc)
    #create the clauses corresponding to "at most one case is true"
    for cas in combinations(nbc,2):
        fau=dict()
        for l in cas:
            fau[l]=False
        nbcl+=1
        res.append(fau)
    return (res,nbcl,var)

#Management of a cell in the border or in the corner of a grid
def cas_cote(i,j,n,t,nbcl,var):
    res=[]
    jus=dict()
    nbc=[]
    c=1
    #corner
    if (i==0 and j==0):
        cases = [(i,  j), (i+1,  j), (i,  j+1),(i+1,  j+1)]
    elif ((i==t-1) and (j==t-1)):
        cases = [(i,  j), (i-1,  j),(i,  j-1), (i-1,  j-1)]
    elif (i==0 and (j==t-1)):
        cases = [(i,  j), (i,  j-1), (i+1,  j), (i+1,  j-1)]
    elif ((i==t-1) and j==0):
        cases = [(i,  j), (i-1,  j), (i,  j+1), (i-1,  j+1)]
    #border
    elif (i==0 and j!=0):
        cases = [(i,  j), (i+1,  j), (i,  j-1), (i,  j+1), (i+1,  j+1), (i+1,  j-1)]
    elif ((i==t-1) and (j!=t-1)):
        cases = [(i,  j), (i-1,  j-1), (i-1,  j),(i,  j-1), (i-1,  j+1), (i,  j+1)]
    elif (i!=0 and j==0):
        cases = [(i,  j), (i+1,  j), (i,  j+1),(i+1,  j+1), (i-1,  j), (i-1,  j+1)]
    elif ((i!=t-1) and (j==t-1)):
        cases = [(i,  j), (i-1,  j), (i,  j-1),(i-1,  j-1), (i+1,  j-1),(i+1,  j)]
    #same as basic case
    for k in combinations(cases,n):
        for p in cases:
            cas=dict()
            if (p in k):
                cas[p]=True
            else:
                cas[p]=False
            cas[(i,j,c)]=False
            nbcl+=1
            res.append(cas)
        c+=1
    c-=1
    o=1
    while (o<=c):
        jus[(i,j,o)]=True
        nbc.append((i,j,o))
        o+=1
    nbcl+=1
    res.append(jus)
    var+=len(nbc)
    for cas in combinations(nbc,2):
        fau=dict()
        for l in cas:
            fau[l]=False
        nbcl+=1
        res.append(fau)
    return (res,nbcl,var)

def crea_cnf(grille,taille):
    t=taille
    #list(=cnf) of lists(=one cell) of dictionnaries(=clauses)
    res=[]
    var=taille**2
    #caculate the number of clauses
    nbcl=0
    for i in range (taille):
        for j in range (taille):
            #list of dictionnaries
            clause=[]
            #management of different cases (0 to 9)
            if (grille[i,j]=='0'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,0,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,0,nbcl,var)
            elif (grille[i,j]=='1'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,1,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,1,nbcl,var)
            elif (grille[i,j]=='2'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,2,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,2,nbcl,var)
            elif (grille[i,j]=='3'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,3,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,3,nbcl,var)
            elif (grille[i,j]=='4'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,4,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,4,nbcl,var)
            elif (grille[i,j]=='5'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,5,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,5,nbcl,var)
            elif (grille[i,j]=='6'):
                if (i==0 or j==0 or (i==t-1) or (j==t-1)):
                    (clause,nbcl,var)=cas_cote(i,j,6,taille,nbcl,var)
                else :
                    (clause,nbcl,var)=cas_normal(i,j,6,nbcl,var)
            elif (grille[i,j]=='7'):
                    (clause,nbcl,var)=cas_normal(i,j,7,nbcl,var)
            elif (grille[i,j]=='8'):
                    (clause,nbcl,var)=cas_normal(i,j,8,nbcl,var)
            elif (grille[i,j]=='9'):
                    (clause,nbcl,var)=cas_normal(i,j,9,nbcl,var)
            if (len(clause)!=0):
                res.append(clause)
    return (nbcl,var,res) #return number of clauses, number of variable and cnf