import numpy
from itertools import combinations

cas=['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97', 'C98', 'C99', 'C100', 'C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C109', 'C110', 'C111', 'C112', 'C113', 'C114', 'C115', 'C116', 'C117', 'C118', 'C119', 'C120', 'C121', 'C122', 'C123', 'C124', 'C125', 'C126']

case=['a','b','c','d','e','f','g','h','i']

def fact(n):
    result=1
    for k in range(1,n+1):
        result*=k
    return result

def crea_dnf():
    l=[]
    l.append('(-a.-b.-c.-d.-e.-f.-g.-h.-i)')
    for k in range(1,9):
        ch="("
        nv=1
        nb=fact(len(case))/fact(k)/fact(len(case)-k)
        for n in combinations(case,k):
            l2=['a','b','c','d','e','f','g','h','i']
            for m in n:
                for o in l2:
                    if (m==o):
                        ch=ch+m+"."
                        l2.remove(m)
            while (len(l2)!=0):
                ch=ch+"-"+l2[0]
                l2.remove(l2[0])
                if (len(l2)!=0):
                    ch=ch+"."
            if (nv!=nb):
                ch=ch+")+("
            nv+=1
        ch=ch+")"
        l.append(ch)
    l.append('(a.b.c.d.e.f.g.h.i)')
    return l



def dnf_cnf(dnf):
    cnf=dict()
    cnf["0"]=dnf[0]
    for i in range(1,9):
        k=0
        ch="("
        ch1="C1"
        for el in dnf[i]:
            if (el=="+"):
                k+=1
                ch1=ch1+"+"+cas[k]
            if (el=="a"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="b"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="c"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="d"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="e"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="f"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="g"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="h"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="i"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="-"):
                ch=ch+"-"
        k+=1
        ch=ch+ch1+")."
        for m in range(k):
            for n in range(m+1,k):
                ch=ch+"(-"+cas[m]+"+-"+cas[n]+")"
                if ((m!=k-2) or (n!=k-1)):
                    ch=ch+"."
        cnf[str(i)]=ch
    cnf["9"]=dnf[9]
    return cnf

def crea_cnf(grille):
    dnf=crea_dnf()
    cnf=dnf_cnf(dnf)
    ch=""
    clauses=0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if (grille[i,j]=='0'):
                ch=ch+cnf.get("0")
                clauses+=1
            if (grille[i,j]=='1'):
                ch=ch+cnf.get("1")
                clauses+=118
            if (grille[i,j]=='2'):
                ch=ch+cnf.get("2")
                clauses+=955
            if (grille[i,j]=='3'):
                ch=ch+cnf.get("3")
                clauses+=4243
            if (grille[i,j]=='4'):
                ch=ch+cnf.get("4")
                clauses+=9010
            if (grille[i,j]=='5'):
                ch=ch+cnf.get("5")
                clauses+=9010
            if (grille[i,j]=='6'):
                ch=ch+cnf.get("6")
                clauses+=4243
            if (grille[i,j]=='7'):
                ch=ch+cnf.get("7")
                clauses+=955
            if (grille[i,j]=='8'):
                ch=ch+cnf.get("8")
                clauses+=118
            if (grille[i,j]=='9'):
                ch=ch+cnf.get("9")
                clauses+=1
            if (((i!=len(grille)-1) or (j!=len(grille)-1)) and (grille[i,j]!=" ")):
                ch=ch+"."
    return (ch,clauses)

