#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:50:18 2025

@author: melusinegeorge
"""
import struct

#Exercice 1 

def extract_sample(nom_fichier):
    F = open( nom_fichier, "rb")
    data = F.read()
    #le nb de canneaux est dans les bits 23,24; ici 2
    #la taille d'un echantillon (sur tous les canneaux) est dans les bits 35,36; ici 16
    #nnb_byts_un_ech = 2
    nb_ech = (len(data)-44)//(4*8)
    ech = []
    for i in range(nb_ech):
       ech_i = struct.unpack_from('hh', data, 44 + 16*i)
       ech.append(ech_i)
    return ech
        
