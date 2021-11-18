# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:29:18 2021

@author: H Persévérance
"""

import pickle 
try:
    with open('file' ,'rb') as file:
        p=pickle.Unpickler(file)
        players=p.load()
except FileNotFoundError:
    players={}
chance=8 
wordlist=['JAMAIS','EFFACER','ASSEOIR','SOUSTRAIRE','ASSERVIR','DEBOUCHER','RETIRER','AVERTIR','OCCUPER'] 
