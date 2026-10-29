"""
Classe définissant les cartes d'un jeu de tarot
"""
class Card :
    def __init__(self, description_suite:str="."):
        # Description obligatoire de la carte
        self._description:str="C'est une carte du jeu de tarot"
        # Description modifiable de la carte
        self._description_suite:str = description_suite

    def getDescription(self):
        return self._description

    def getDescriptionSuite(self):
        return self._description_suite

    def setDescriptionSuite(self, desc:str):
        self._description_suite = desc

    def __str__(self):
        return "Description  : "+self._description+self._description_suite+"\n"