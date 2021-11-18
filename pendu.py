# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:41:04 2021

@author: H Persévérance
"""
import donnees as d 
from random import choice 
import fonctions as f
import os

g=1
while g==1:
    print("Welcome to the game of Pendu\n")
    nom=input("Enter your name?: ") 
    score=0
    nb_chance=d.chance
    if nom in d.players.keys():
        score=d.players[nom]
        print(nom+', your recent score is ',score)
    else:
        print(nom+', your score is ',score) 
    word=choice(d.wordlist)
    upword=f.hideword(word)
    while nb_chance>0 and upword!=word:
        print('Find the word of {0} letter :{1}\nYou have {2} chance\n'.format(len(word),upword, nb_chance))
        newletter=input("Enter a letter in the hided word : ").upper()
        if (newletter in word) and not(newletter in upword) :
            upword=f.letter_found(word,newletter, upword)
        else:
            print(newletter+'is not in the right word\nYou have now %d chance \n',nb_chance)
            nb_chance-=1
    f.save(nom,nb_chance)
    if upword==word:
        print("Congratulation, Your score is ",nb_chance)
    else:
        print("You have lost")
    
    g=int(input("Voulez-vous continuer? Entrez 1 pour continuer et 0 pour quitter ") )


os.system('pause')
