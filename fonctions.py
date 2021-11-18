# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:42:26 2021

@author: H Persévérance
"""

import pickle


def save(name,score=0):
    try:
        with open('file' ,'rb') as file:
            p=pickle.Unpickler(file)
            players=p.load()
    except FileNotFoundError:
        players={}
    players[name]=score
    with open('file' ,'wb') as file:
        p=pickle.Pickler(file)
        p.dump(players)
        

def hideword(word):
    hiddenWord=""
    for i in range(len(word)):
        hiddenWord+='*'
    return hiddenWord

def letter_found(word,letter, upword):
    wd=""
    for k,i in enumerate(word):
        if i==letter :
            wd+=i
        else:
            wd+=upword[k]
    upword=wd
    return upword
