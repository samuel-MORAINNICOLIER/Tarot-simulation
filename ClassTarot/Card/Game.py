from random import shuffle, randint
from ClassTarot.Card.Card import *

"""
Définit la pile contenant les cartes du jeu de tarot
"""
class Game :
    _jeu = []

    def getPile(self):
        return self._jeu

    def getRandCard(self):
        return self._jeu[randint(0, len(self._jeu)-1)]

    def addCard(self, card:Card):
        """
        Permet de rajouter des cartes à la pile
        :param card: Carte à rajouter
        :return: None
        """
        self._jeu.append(card)

    def delCard(self,card:Card):
        self._jeu.remove(card)

    def mixPile(self):
        shuffle(self._jeu)

    def couperPile(self, i_carte:int)->bool:
        """
        Permet de couper la pile en deux et de la reconstituer en inversant les deux parties
        :param i_carte: Indice de la carte constituant la séparation (on sépare entre cette carte et la suivante)
        :return: True si la coupe a pu être éffectuer et False sinon
        """
        coupe = False
        if i_carte >=0 and i_carte < (len(self._jeu)-1):
            coupe = True
            partie_1 = []
            partie_2 = []
            for i in range(i_carte):
                partie_1.append(self._jeu[i])
            for i in range(i_carte, len(self._jeu)):
                partie_2.append(self._jeu[i])
            self._jeu = partie_2 + partie_1
        return coupe

    def __str__(self):
        rep = "Pile : [ \n"
        for carte in self._jeu:
            rep += str(carte)+" \n"
        rep += "] \n"
        return rep