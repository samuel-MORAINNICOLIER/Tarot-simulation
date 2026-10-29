from ClassTarot.Card.MinorArcane import *
"""
Classe définissant les cartes standards (1, 2, ..., 10)
qui font partie des arcanes mineures d'un jeu de tarot
"""
class Standard(MinorArcane) :
    def __init__(self, couleur:str, nombre:int, description_suite:str="."):
        # Appel au constructeur de la classe parente
        super().__init__(couleur,description_suite)
        # Nombre de la carte (1,2,3...,10)
        self._nombre:int = nombre
        # Description obligatoire de la carte
        self._description:str = "Cette carte est le "+str(self._nombre)+" de "+str(super().getCouleur())
        # Image
        self._image:str = "Images/Cards/"+str(couleur)+"/"+str(couleur)+str(nombre)+".png"

    def getNombre(self):
        return self._nombre

    def getLienImage(self):
        return self._image

    def __str__(self):
        rep = super().__str__()
        rep += "Nombre  : "+str(self._nombre)+"\n"
        return rep