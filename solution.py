from tkinter import *

#in this file using the generated random grid and the sat result we display the filled grid

def resolution_grille(NB_DE_CASES,grille):
    r = open("dimacs.txt", "r")

    solver = r.readline()                               #We read the first line #
                                                        #We read line by line until the first character is "s" #
                                                        #This is due to the format returned by the SAT #
                                                        #The line where we know if it's SAT or UNSAT at the first car "s" #
                                                        #All the lines ahead we go first because "c" #

    while solver[0]!="s":
        solver = r.readline()
    if solver[2] != "S":                                #if the third one (the "s" and " " because from this line is not S for SAT
        print("There is no solution to this one")       #So there are no solutions to the generated grid

    else:
        fen = Tk()
        COTE = 500
        MARGE = 0                                       # here we set the Tkinter page used to display the solution
        DECALAGE = 20
        PAS = COTE / NB_DE_CASES
        can = Canvas(fen, bg="light gray", height=(COTE + MARGE), width=2 * (MARGE + COTE) + DECALAGE)
        can.pack()

        #here we'll create a first grid on the left of the tkinter page
        a = 0
        while (a <= NB_DE_CASES):
            can.create_line(COTE + DECALAGE, PAS * a, DECALAGE + (COTE * 2), PAS * a, fill='black')
            x = 0
            while (x <= NB_DE_CASES):
                can.create_line(0, PAS * x, COTE, PAS * x, fill='black')
                x = x + 1

            y = 0
            while (y <= NB_DE_CASES):
                can.create_line(PAS * y, 0, PAS * y, COTE, fill='black')
                y = y + 1
            can.create_rectangle(1.5, 1.5, COTE, COTE)


            # here we're going to fill the initial grid on the tkinter page with the basic generated grid
            for i in range(NB_DE_CASES):
                for j in range(NB_DE_CASES):
                    can.create_text(((PAS) / 2) + ((PAS) * i), (((PAS) / 2) + (PAS) * j), text=grille[j][i])
            can.create_rectangle(1.5, 1.5, COTE, COTE)
            a = a + 1

        b = 0
        while (b <= NB_DE_CASES):
            can.create_line(PAS * b + DECALAGE + COTE, 0, PAS * b + DECALAGE + COTE, COTE, fill='black')
            b = b + 1

        # The initial grid was done, now we're doing the final grid
        # for this we will use the file obtained with the sat


        var = 1
        h = 0
        l = 0
        compteur=0

        solver2 = r.readline()                  #The line below SAT contains the model
                                                #Each value corresponds to a box, line by line.

        while compteur <= (NB_DE_CASES)**2:     # NB_DE_CASES must be squared to obtain the total number of boxes
                                                # We're entering a while loop with an iterating counter
                                                #counter corresponds to the box numbers so, line by line


            if solver2.split()[var][0] == "-":  #if the variable is preceded by a "-" it means that the box does not have to
                                                #be colourful

                can.create_rectangle(PAS * l + DECALAGE + COTE, PAS * h, PAS * l + DECALAGE + COTE + PAS, PAS * h + PAS,
                                     fill='white')

                                                # So it's represented by a white box, so that's why we create it
                                                # a white square using the dimensions etc from the tkinter page,
                                                # Then we fill it in blank #

                var = var + 1
                l = l + 1
                if (l) % NB_DE_CASES == 0:  #this if loop lets you know when to go to the next line
                    h = h + 1                     #which will therefore allow us to adapt
                    l = 0

            else:
                can.create_rectangle(PAS * l + DECALAGE + COTE, PAS * h, PAS * l + DECALAGE + COTE + PAS, PAS * h + PAS,
                                     fill='black')
                                                  # If there is no minus, the box must be filled in
                                                  # So we do the same thing by filling  the rectangle in black
                var = var + 1
                l = l + 1
                if (l) % NB_DE_CASES == 0:
                    h = h + 1
                    l = 0
            try:
                solver2.split()[var][0] #try if solver2.split()[var][0] raise an error
            except IndexError:          #if we have IndexError, take the next line in the file and save var in compteur and put var=1 to restart the previous operation
                solver2=r.readline()
                compteur+=var
                var=1

        can.create_rectangle((COTE + DECALAGE), 1.5, 2 * (MARGE + COTE) + DECALAGE, COTE)
        fen.mainloop() #necessary to use tkinter
    r.close() #close r