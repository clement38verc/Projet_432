import numpy
from itertools import combinations

def cas_normal(i,j,n,nbcl,var):
    res=[]
    jus=dict()
    nbc=[]
    c=1
    cases = [(i,  j), (i+1,  j), (i-1,  j), (i,  j+1),(i+1,  j+1), (i-1,  j+1), (i,  j-1), (i+1,  j-1), (i-1,  j-1)]
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

def cas_cote(i,j,n,t,nbcl,var):
    res=[]
    jus=dict()
    nbc=[]
    c=1
    if (i==0 and j==0):
        cases = [(i,  j), (i+1,  j), (i,  j+1),(i+1,  j+1)]
    elif ((i==t-1) and (j==t-1)):
        cases = [(i,  j), (i-1,  j),(i,  j-1), (i-1,  j-1)]
    elif (i==0 and (j==t-1)):
        cases = [(i,  j), (i,  j-1), (i+1,  j), (i+1,  j-1)]
    elif ((i==t-1) and j==0):
        cases = [(i,  j), (i-1,  j), (i,  j+1), (i-1,  j+1)]
    elif (i==0 and j!=0):
        cases = [(i,  j), (i+1,  j), (i,  j-1), (i,  j+1), (i+1,  j+1), (i+1,  j-1)]
    elif ((i==t-1) and (j!=t-1)):
        cases = [(i,  j), (i-1,  j-1), (i-1,  j),(i,  j-1), (i-1,  j+1), (i,  j+1)]
    elif (i!=0 and j==0):
        cases = [(i,  j), (i+1,  j), (i,  j+1),(i+1,  j+1), (i-1,  j), (i-1,  j+1)]
    elif ((i!=t-1) and (j==t-1)):
        cases = [(i,  j), (i-1,  j), (i,  j-1),(i-1,  j-1), (i+1,  j-1),(i+1,  j)]
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
    res=[]
    var=taille**2
    nbcl=0
    for i in range (taille):
        for j in range (taille):
            clause=[]
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
    return (nbcl,var,res)