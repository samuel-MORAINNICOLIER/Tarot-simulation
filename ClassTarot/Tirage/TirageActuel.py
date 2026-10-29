#from TiragePossible import *
from ClassTarot.Card.Card import *
from ClassTarot.Card.Game import *
"""
Classe qui représente les cartes tirées
"""
class TirageActuel :
    def __init__(self):
        # Cartes tirées /présentes sur le plateau
        self._card_tire:list = []
        # Liste des tirages possibles
        self._tirages_possibles:list = []
        # Booléen qui indique si les cartes sont retournées ou non
        self._retourne:bool = False

    def getCardTire(self):
        return self._card_tire

    def getTiragePossibles(self):
        return self._tirages_possibles

    def getRetourne(self):
        return self._retourne

    def getTiragePossibleActuel(self):
        """
        Renvoie le tirage utilisable en fonction du nombre de cartes tirée
        :return: renvoie le tirage ou None si aucun correspond
        """
        tirage = None
        if len(self._tirages_possibles) > len(self._card_tire):
            tirage =  self._tirages_possibles[len(self._card_tire)]
        return tirage

    def piocherDepuis(self, card:Card, pile:Game):
        self._card_tire.append(card)
        pile.delCard(card)

    def piocherDepuisRand(self, pile:Game):
            self.piocherDepuis(pile.getRandCard(),pile)

    def addTiragePossibles(self, tirage):
        self._tirages_possibles.append(tirage)

    def retourneCard(self):
        self._retourne = not self._retourne

    def DireLAventure(self)->list:
        """
        Renvoie la bonne aventure en fonction des cartes tirées et du tirage correspondant au nombre de cartes tirées
        :return:
        """
        nbCarteTire= len(self._card_tire)
        aventure = []
        tirage = None
        for tiragePossible in self._tirages_possibles:
            if tiragePossible.getNbCard() == nbCarteTire :
                tirage = tiragePossible
                for i_carte in range(nbCarteTire):
                    aventure.append((tirage.getEffetCard()[i_carte], self._card_tire[i_carte].getDescription()))
        return aventure

    def __str__(self):
        rep = "> Cartes présentes : \n"
        for card in self._card_tire:
            rep += str(card)
        rep += "> Tirages enregistrées : \n"
        for tirage in self._tirages_possibles:
            rep += str(tirage)
        if self._retourne :
            rep += "> Les cartes sont face visibles\n"
        else :
            rep += "> Les cartes présentes sont de dos\n"
        return rep