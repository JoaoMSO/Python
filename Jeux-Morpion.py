# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:59:39 2025

@author: JMSO

"""
Lt=[
    ['X',1,2,3],
    ['a',0,0,0],
    ['b',0,0,0],
    ['c',0,0,0]
]
mouv_let = 0
mouv_num = 0
Etat = True
nbr_pt = 0

def ecran ():           #fonction qui permet d'afficher le tableau
    for i in range(0,4):
        a = Lt[i]
        print(a)

def Mouv_Y():         #fonction qui permet de choisir un mouvement sur l'axe des y
    mouv_let=input('choisies une lettre ....         ')
    match mouv_let:
        case 'a':
            return 1
        case 'b':
            return 2
        case 'c':
            return 3


def Mouv_X():        #fonction qui permet de choisir un mouvement sur l'axe des x
    mouv_num=int(input('choisies un chiffre ....     '))
    return mouv_num

def Partie(mouv_let, mouv_num):         #fonction qui permet de jouer
    if mouv_let != 0 and mouv_num != 0 :
        Lt[mouv_let][mouv_num] = 1

def main_loop():     #fonction princupale
    while Etat:
        ecran()
        mouv_let = Mouv_Y()
        mouv_num = Mouv_X()
        Partie(mouv_let, mouv_num)
        nbr_pt += 1
        if nbr_pt == 9:
            Etat = False

Etat = True
nbr_pt = 0
Lt = [
    ['X', 1, 2, 3],
    ['a', 0, 0, 0],
    ['b', 0, 0, 0],
    ['c', 0, 0, 0]
]

        
main_loop()
    