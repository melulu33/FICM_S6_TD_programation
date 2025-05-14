#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:56:48 2025

@author: melusinegeorge
"""

from tkinter import Tk, Canvas
import numpy as np
from random import random



#                               Exercice 1
WIDTH = 500
HEIGHT = 500
G = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
pos = np.array([(random()*WIDTH, random()*HEIGHT) for i in range(len(G))])
vit = np.array([((random()-0.5)*10, (random()-0.5)*10)for i in range(len(G))])



#exemple de dessin (donne par le prof dans le td )
def draw(can, graph, pos):
    can.delete("all")
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
    can.update()

#                               Exercice 2 

#constantes 
k = 0,1
l0 = 10
m = 1


def forces_sur_sommets(pos):
    forces = np.array([(0, 0) for i in range(len(G))])
    for i in range(len(G)):
        F_sur_i = [0,0] #vectorielle
        for j in G[i]:
            l = ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)**(1/2)
            F_sur_i[0] += k * (l - l0) * (pos[i][0] - pos[j][0]) / l
            F_sur_i[1] += k * (l - l0) * (pos[i][1] - pos[j][1]) / l
        forces[i] = F_sur_i
    return forces

def maj_position(pos):
    forces = forces_sur_sommets(pos)
    for i in forces:
        vitesse = [i[0]+vit, i[1]]
        pos[i][0], pos[i][1] = pos[i][0] + vitesse[0], pos[i][1]+vitesse[1]
    

def clavier_f():
    maj_position(pos)
    can.delete("all")
    draw(can, G, pos)
        


root = Tk()
root.title("dessin de graph")
can = Canvas(root, width = WIDTH, height = HEIGHT)
can.grid(column=1, row=0, columnspan=2, padx = 10, pady=10)
draw(can, G, pos)
root.bind("<f>",lambda e:clavier_f())
root.mainloop()

## J'ai fermé python et le code ne veut meme plus s'executer ... voici l'erreur annoncée
''''TclError: Can't find a usable init.tcl in the following directories: 
    /usr/local/Cellar/tcl-tk/8.6.13_5/lib/tcl8.6 /Applications/Spyder.app/Contents/lib/tcl8.6 /Applications/Spyder.app/lib/tcl8.6 /Applications/Spyder.app/Contents/library /Applications/Spyder.app/library /Applications/Spyder.app/tcl8.6.13/library /Applications/tcl8.6.13/library
    
This probably means that Tcl wasn't installed properly.'''