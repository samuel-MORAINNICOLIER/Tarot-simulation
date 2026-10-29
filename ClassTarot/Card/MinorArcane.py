from ClassTarot.Card.Card import *
"""
Classe définissant les arcanes mineures d'un jeu de tarot
"""
class MinorArcane(Card) :

    def __init__(self, couleur:str = "bouclier"or"baton"or"epee"or"coupe", description_suite:str="."):
        # Appel au constructeur de la classe parente
        super().__init__(description_suite)
        # Couleur de la carte (Ecu,Baton,...,Coupe)
        self._couleur:str=couleur
        # Description obligatoire de la carte
        self._description:str = "Cette carte fait partie de la famille des "+str(self._couleur)

    def getCouleur(self):
        return self._couleur

    def __str__(self):
        rep = super().__str__()
        rep += "Couleur : "+self._couleur+"\n"
        return rep