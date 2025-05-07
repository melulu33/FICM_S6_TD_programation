#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:50:52 2025

@author: melusinegeorge
"""

from tkinter import Tk, Canvas, Button

class App :
    
    def __init__(self, data, largeur, hauteur):
        self.root = Tk('hello')
        self.data = data
        self.largeur = largeur
        self.hauteur = hauteur
        self.can = Canvas(self.root, width=self.largeur, height=self.hauteur, bg = 'white')
        self.couleurs = ["yellow", "orange", "pink", "purple"]
        
        
    def run_forever(self):
        self.can.grid(column=1, row=0, columnspan=2, padx = 10, pady=10)
        self.can.update()
        App.redraw(self)
        def swap_colors():
            #global self.colors
            cp = []
            for i in range(1, len(self.colors) + 1):
                cp.append(self.colors[i % len(self.colors)])
            self.colors = cp
            App.redraw(self)
        Button(self.root, text="Quit", command=lambda: self.root.quit()).grid(column=1, row=2)
        Button(self.root, text="Colors", command = lambda : swap_colors()).grid(column=2, row=2)
        self.root.mainloop()
    
       
    def redraw(self):
        #nettoyer le canvas
        self.can.delete("all")
        #dessiner les fils
        W = int( self.largeur / len(self.data.mot_entrelas[0]))
        H = int( self.hauteur / (len(self.data.mot_entrelas) + 1))
        for i, word in enumerate(self.data.mot_entrelas):
            x = 0
            y = H*(i+1) 
            for lettre in word:
                if lettre == 'H':
                    Canvas.create_line(self.can, x, y, x + H,y,fill=self.colors[i])
                    x = x + H
                if lettre == 'U':
                    Canvas.create_line(self.can, x, y, x + H,y - W,fill=self.colors[i])
                    x = x + H
                    y = y - W
                if lettre == 'D':
                    Canvas.create_line(self.can, x, y, x + H, y + W,fill=self.colors[i])
                    x = x + H
                    y = y + W


class Data:
    
    def __init__(self, nb_fils, mot_entrelas):
        self.nb_fils = nb_fils
        self.mot_entrelas = mot_entrelas


    def tab_to_words(tableau, nombre):
        out_words = ["H"] * nombre
        pi = list(range(nombre))
        for cross in tableau:
            permutate = pi[cross]
            permutateNext = pi[cross + 1]
            out_words = [c + ("D" if i == permutate else "U" if i == permutateNext else "H") + "H" for i, c in enumerate(out_words)]
            pi[cross], pi[cross + 1] = pi[cross + 1], pi[cross]
        return Data(nombre, out_words)
    
    
if __name__ == "__main__":
    crossings = [2, 1, 1, 0, 2]
    data = Data(4, Data.tab_to_words(crossings,4))
    app = App( data, 150, 150)
    App.run_forever(app)
    
    