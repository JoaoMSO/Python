# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:59:39 2025

@author: JMSO

"""
Lt=[['X',1,2,3],['a',0,0,0],['b',0,0,0],['c',0,0,0]]
mouv_let = 0
mouv_num = 0
partie = True
nbr_pt = 0

def ecran ():
    for i in range(0,4):
        a = Lt[i]
        print(a)

def Mouv_Y():
    mouv_let=input('choisies une lettre ....')
    match(mouv_let):
        case 'a':
            return int(1)
        case 'b':
            return int(2)
        case 'c':
            return int(3)

def Mouv_X():
    mouv_num=int(input('choisies un chiffre ....'))
    return mouv_num

def Partie():
    if mouv_let != 0 and mouv_num != 0 :
        Lt[mouv_let][mouv_num] = 11111111111111111

def main_loop():
    while partie == True:
        ecran()
        mouv_let=Mouv_Y()
        mouv_num = Mouv_X()
        Partie()
        
        
main_loop()
    
"""
['X',1,2,3]
['a',0,0,0]
['b',0,0,0]
['c',0,0,0]
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"
"""