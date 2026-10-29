"""
Classe qui représente les tirages possibles
"""
class TiragePossible :
    def __init__(self, nom:str, effet_card:list):
        """
        Initialise les attributs d'un tirage possible
        :param nom: La description du tirage possible
        :param effet_card: Liste des effets de chaque carte du tirage
        """
        self._nom:str = nom
        self._effet_card:list = effet_card
        # nombre de cartes du tirage
        self._nb_card:int = len(self._effet_card)

    def getNom(self):
        return self._nom

    def getEffetCard(self):
        return self._effet_card

    def getNbCard(self):
        return self._nb_card

    def __str__(self):
        rep  = "Nom             : "+str(self._nom)+"\n"
        rep += "Nombre de carte : "+str(self._nb_card)+"\n"
        for i in range(len(self._effet_card)):
            rep += "Carte numero "+str(i+1)+"  : "+str(self._effet_card[i]+"\n")
        return rep