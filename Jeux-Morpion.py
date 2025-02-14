# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:59:39 2025

@author: JMSO

"""

class MorpionGame:
    def __init__(self):
        self.Lt = [
            ['X', 1, 2, 3],
            ['a', '/','/', '/'],
            ['b', '/', '/', '/'],
            ['c', '/','/', '/']
        ]
        self.mouv_let = 0
        self.mouv_num = 0
        self.Etat = True
        self.nbr_pt = 0
        self.X = 'X'
        self.O = '0'
        

    def ecran(self):  # fonction qui permet d'afficher le tableau
        for i in range(0, 4):
            a = self.Lt[i]
            print(a)

    def Mouv_Y(self):  # fonction qui permet de choisir un mouvement sur l'axe des y
        mouv_let = input('choisies une lettre ....         ')
        match mouv_let:
            case 'a':
                return 1
            case 'b':
                return 2
            case 'c':
                return 3

    def Mouv_X(self):  # fonction qui permet de choisir un mouvement sur l'axe des x
        mouv_num = int(input('choisies un chiffre ....     '))
        return mouv_num

    def Partie(self, mouv_let, mouv_num):  # fonction qui permet de jouer
        if mouv_let != 0 and mouv_num != 0:
            if self.nbr_pt % 2 == 0:
                self.Lt[mouv_let][mouv_num] = self.X
            else:
                self.Lt[mouv_let][mouv_num] = self.O

    def main_loop(self):  # fonction principale
        while self.Etat:
            self.ecran()
            mouv_let = self.Mouv_Y()
            mouv_num = self.Mouv_X()
            self.Partie(mouv_let, mouv_num)
            self.nbr_pt += 1
            if self.nbr_pt == 9:
                self.Etat = False


if __name__ == "__main__":
    game = MorpionGame()
    game.main_loop()
