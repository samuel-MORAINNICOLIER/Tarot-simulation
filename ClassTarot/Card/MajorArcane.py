from ClassTarot.Card.Card import *
"""
Classe définissant les arcanes majeures d'un jeu de tarot
"""
class MajorArcane(Card) :
    def __init__(self, numero:int, nom:str, description_suite="."):
        # Appel au constructeur de la classe parente
        super().__init__(description_suite)
        # Numero de la carte (de 1 à 22)
        self._numero:int = numero
        # Nom de la carte (Hermite, Chariot...)
        self._nom:str = nom
        # Description obligatoire de la carte
        self._description:str = "Cette carte représente "+str(self._nom)+" et est le numéro "+str(self._numero)

    def getNumero(self):
        return self._numero

    def getNom(self):
        return self._nom

    def __str__(self):
        rep = super().__str__()
        rep += "Numero  : "+str(self._numero)+"\n"
        rep += "Nom     : "+self._nom+"\n"
        return rep