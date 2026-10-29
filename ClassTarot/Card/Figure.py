from ClassTarot.Card.MinorArcane import *
"""
Classe définissant les figures (valet, cavalier, reine, roi)
qui font partie des arcanes mineures d'un jeu de tarot
"""
class Figure(MinorArcane) :
    def __init__(self, couleur:str, nom:str, description_suite:str="."):
        # Appel au constructeur de la classe parente
        super().__init__(couleur,description_suite)
        # Nom de la figure (valet,...,roi)
        self._nom:str = nom
        # Description obligatoire de la carte
        self._description:str = "Cette carte représente le "+str(self._nom)+" de "+str(super().getCouleur())
        # Image
        self._image: str = "Images/Cards/"+str(couleur)+"/"+str(couleur)+str(nom)+".png"

    def getNom(self):
        return self._nom

    def getLienImage(self):
        return self._image

    def __str__(self):
        rep = super().__str__()
        rep += "Nom     : "+self._nom+"\n"
        return rep