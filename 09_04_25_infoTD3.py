#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:04:13 2025

@author: melusinegeorge
"""

## Exercice 1
''' Tree doit pouvoir:
initialiser un aobjet de la classe
parcourir l'arbre 
extraire un noeuds et son etiquette 
extraire les fils d'un noeud
'''

## Exercice 2
class Tree:
    def __init__(self,symbol,*children):
        self.__children = children
        self.__symbol = symbol
    
    def label(self)->str:
        return self.__symbol
    
    def children(self)-> tuple:
        return self.__children
    
    def nb_children(self)->int:
        return len(self._children)
    
    def child(self, i:int) -> Tree:
        return self.__children(i)
    
    def is_leef(self) -> bool:
        return len(self.__children)==1
    
## j'ai rien compris mais je vais travailler tout ca la semaine prochaine

    
        