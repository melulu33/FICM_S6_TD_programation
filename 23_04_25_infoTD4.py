#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:51:53 2025

@author: melusinegeorge
""" 
import matplotlib.pyplot as plt


# Exercice 2 


def h_naif(a):
    '''fonction de hachage naive '''
    if type(a) != str :
        return None
    else:
        hache = 0
        for lettre in a:
            hache += ord(lettre)
        return hache


class Hashtable:
    
    def __init__(self, f_hache, taille):
        '''self est une fonction de hachage'''
        self.taille = taille
        self.f_hache = f_hache
        self.liste_hachage = [ [] for i in range(taille)]
        
        
    
    def put(self, key, value):
        '''Cette méthode insère un nouveau couple (key,value)dans la table si la clé ne s'y trouve pas déjà. 
        Sinon, elle met à jour la valeur associée à la clé.'''
        indice = self.f_hache(key)%self.taille
        
        for i in range(len(self.liste_hachage[indice])):
            if key == self.liste_hachage[indice][i][0]:
                self.liste_hachage[indice][i][1] = value
                return 'Fait'
        self.liste_hachage[indice].append( (key, value))
        return 'Fait'
            
    # Exercice 3
    def get(self, key):
        indice = self.f_hache(key)%self.taille
        for i in range(len(self.liste_hachage[indice])):
            if key == self.liste_hachage[indice][i][0]:
                return self.liste_hachage[indice][i][1]
        return None
       
    # Exercice 4
    def repartition(self):
        tailles = [len(truc) for truc in self.liste_hachage]
        N = self.taille
        x = range(N)
        width = 1/1.5
        plt.bar(x, tailles, width, color="blue")
        plt.show()
                     
# tests 

#repris du TD1
f = open("frenchssaccent.dic",'r')
dico = list()
for ligne in f:
    dico.append(ligne [ 0 : len(ligne)-1 ] )
f.close()



ht = Hashtable(h_naif,10000)

for mot in dico:
    ht.put(mot, len(mot))
    
ht.repartition()

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                