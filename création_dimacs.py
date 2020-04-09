import os

pos=['a','b','c','d','e','f','g','h','i','C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97', 'C98', 'C99', 'C100', 'C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C109', 'C110', 'C111', 'C112', 'C113', 'C114', 'C115', 'C116', 'C117', 'C118', 'C119', 'C120', 'C121', 'C122', 'C123', 'C124', 'C125', 'C126']

def crea_dimacs(nbclaus,c):
    d=open("Dimacs.cnf", "w")
    d.write("p cnf 135 "+str(nbclaus)+"\n")
    n=0
    for el in c:
        if (el == "."):
            d.write(" 0\n")
        if (el=="+"):
            d.write(" ")
        if (el=="-"):
            d.write(el)
        if (el=="a"):
            d.write(str(1))
        if (el=="b"):
            d.write(str(2))
        if (el=="c"):
            d.write(str(3))
        if (el=="d"):
            d.write(str(4))
        if (el=="e"):
            d.write(str(5))
        if (el=="f"):
            d.write(str(6))
        if (el=="g"):
            d.write(str(7))
        if (el=="h"):
            d.write(str(8))
        if (el=="i"):
            d.write(str(9))
        if (el=="C"):
            k=n
            ch=""
            while ((c[k]!=")") and (c[k]!="+")):
                ch=ch+c[k]
                k+=1
            d.write(str(pos.index(ch)+1))
        n+=1
    d.write(" 0")
    d.close()