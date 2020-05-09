# Projet_432
projet_kevin_clement 

The user must execute main.py without argument under Linux system or Windows Subsystem for Linux.

The user have to choose between the using of our generator of a grid and his/her own grid with the size.

Generator : create a random grid with a size between 1 and 10 with the format np.array. We can change it line 32 (NB_DE_CASES_MAX=).
More the size is big, more we advise the augmentations of space in lines 24, 25 and 26 to have more luck to obtain a satisfiable grid.

Personal : The grid must be in a file  in a format .txt. Like in the example grille.txt, the cells in the same line must be separated by
a tabulation \t :
1	 	2
 	 	 
2	 	1

The user must be precised the size after not in the file.

Finally, the user have 2 grids if it is satisfiable. One with numbers and the other with the cells white or black. The grid must be closed
to take the control of the console.
If it is unsatisfiable, the user have a message on the console.