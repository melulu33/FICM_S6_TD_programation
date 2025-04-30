#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:50:12 2025

@author: melusinegeorge
"""

from tkinter import Tk, Canvas, Button
    

## EXERCICE 1

def read_word(canvas, mot, h, w):
    ''' interpreter un mot composé de H,U,D ( si autre lettres il ne reagit pas)
    ATTENTION je ne sais pas comment gerer les dimentions du canvas il risque d'y avoir des depassements celon les valeurs de h et w'''
    x = 0
    y = 50 # je sais pas comment appeller height/2 donc je mets la valeur numerique 
    for lettre in mot:
        if lettre == 'H':
            Canvas.create_line(canvas, x, y, x + h,y,fill='blue')
            x = x + h
        if lettre == 'U':
            Canvas.create_line(canvas, x, y, x + h,y - w,fill='blue')
            x = x + h
            y = y - w
        if lettre == 'D':
            Canvas.create_line(canvas, x, y, x + h, y + w,fill='blue')
            x = x + h
            y = y + w
    return canvas

def test_1():
    root = Tk('hello')
    root.title('Exercice 1')
    can = Canvas(root, width=100, height=100, bg = 'white')
    can.grid( column = 1, row = 1)
    read_word(can, 'HUHHDUH' , 5, 3)
    root.mainloop()

## EXERCICE 2

def read_word_debut_variable(canvas, mot, h, w, debut):
    ''' interpreter un mot composé de H,U,D ( si autre lettres il ne reagit pas)'''
    x = 0
    y = debut # je sais pas comment appeller height/2 donc je mets la valeur numerique 
    for lettre in mot:
        if lettre == 'H':
            Canvas.create_line(canvas, x, y, x + h,y,fill='blue')
            x = x + h
        if lettre == 'U':
            Canvas.create_line(canvas, x, y, x + h,y - w,fill='blue')
            x = x + h
            y = y - w
        if lettre == 'D':
            Canvas.create_line(canvas, x, y, x + h, y + w,fill='blue')
            x = x + h
            y = y + w
    return canvas

def exo2(canvas, tableau, nombre):
    ''' transforme un tableau et un nombre en mots à tracer '''
    mots = {}
    
    # initialisation
    for i in range(nombre):
        mots = ['H' for i in range(nombre)]
    #on renverse le tableau     
    tableau_renverse = tableau[::-1] # on lit la liste à l'envers
    
    for k in tableau_renverse:
        if k+2 > nombre : return 'NOMBRE NON COMPATIBLE AVEC LE TABLEAU' 
        mots[k] += 'D' # la k+1 descend 
        mots[k+1] += 'U' # la k+2 monte
        mots[k],mots[k+1] = mots[k+1],mots[k] # l'ancienne (k+2)-ieme ligne devient la nouvelle (k+1)-ieme 
        for i in range(nombre):
            if i != k+1 and i != k+2:
                mots[i] += 'H' # les autres vont tout droit
        # puis tout le monde va tout droit
        for i in range(nombre):
            mots[i] += 'H'
        
    #tracer
    h = 50
    w = 50
    for i in range(nombre):
        read_word_debut_variable(canvas, mots[i], h, w, w*(i+1))
    print(mots)


def test_2():
    root = Tk('hello')
    root.title('Exercice 2')
    can = Canvas(root, width=1000, height=1000, bg = 'white')
    can.grid( column = 1, row = 1)
    exo2(can, [2, 1, 1, 0, 2], 4)
    root.mainloop()
    
## sur cet exo il faut que je corrige le code 
    