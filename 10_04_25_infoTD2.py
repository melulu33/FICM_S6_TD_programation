#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 11:54:07 2025

@author: melusinegeorge
"""

## TD2 peogramation 

import unittest

#Exercice 1
## REPRIS AVEC LA CORRECTION

class Polynomial:
    ''' on suppose que le coefficient de degre i le i eme du tuple coeff'''
    # on aurrait pu faire l'hypothese que le premier du tuple est non nul et le terme de plus haut degre 
    def __init__(self,*coeff):
        self.coeff = coeff # je n'ai pas besoin que ce soit autre chose quun tuple 
        
        
    def __str__(self):
       monomes = []
       for i in range(len(self.coeff)-1, -1, -1):
           a = self.coeff[i]
           if a == 0:
               continue
           monomes.append(f"{a}*X^{i}")
       if len(monomes)==0:
           return "0"
       polynome = ' + '.join(monomes)
       polynome = polynome.replace(' + -',' - ').replace('X^1','X').replace('X^0','').replace('1*','')
       return polynome             


    def add(self, other):
        #et la je suis heureuse d'avoir fait l'hypothese du ieme terme = ieme degre 
        somme_coeff = []
        for i in range(max (len(self.coeff),len(other.coeff))):
            if i>=len(self.coeff):
                somme_coeff.append(other.coeff[i])
            if i>=len(other.coeff):
                somme_coeff.append(self.coeff[i])
            else:
                somme_coeff.append(self.coeff[i]+other.coeff[i])
        return Polynomial(*somme_coeff)


class TestPolynomial(unittest.TestCase):
    
    def test_str(self):
        self.assertEqual(str(Polynomial([0, -1, 2])), "2*X^2 - X")
        self.assertEqual(str(Polynomial([0, 0, 0])), "0")
        self.assertEqual(str(Polynomial([1])), "1")
        self.assertEqual(str(Polynomial([-1])), "-1")
        self.assertEqual(str(Polynomial([0,1])), "X")
        self.assertEqual(str(Polynomial([0,-1])), "-X")
        self.assertEqual(str(Polynomial([0,2])), "2*X")
        self.assertEqual(str(Polynomial([1,0,1])), "X^2 + 1")
        self.assertEqual(str(Polynomial([1, 2, 3])), "3*X^2 + 2*X + 1")
        # bon la j'ai copie colle les tests :) 
        
    def test_add(self):
        p1 = Polynomial(1,2,3)
        p2 = Polynomial(12,23,34,4,4)
        self.assertEqual(p1.add(p2),Polynomial(13,25,37,4,4))
        self.assertEqual(p1.add(p2),p2.add(p1))
        

#Exercice 2 
    
class NQpolynomial:
    
    def __init__(self,n,q,*coeff):
        self.q = q
        self.n = n
        self.coeff = [coeff[i] % q for i in range(len(coeff))]
        
    def __str__(self):
        polynome = ' '
        for i in range(len(self.coeff)):
            if self.coeff[i] != 0:
                a = str(self.coeff[i])
                puissance = str(i)
                polynome = polynome + a + 'X^' + puissance + ' '
                if i != len(self.coeff) - 1 :
                    polynome = polynome + '+'
        return polynome          