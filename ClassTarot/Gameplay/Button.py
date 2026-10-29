import pygame
"""
Définit les boutons dans l'interface du jeu
"""
class Button :
    def __init__(self,image_normale:pygame.Surface, image_appuye:pygame.Surface,position:tuple|list, hit_box:tuple):
        self._image_normale:pygame.Surface = image_normale
        self._image_appuye:pygame.Surface = image_appuye
        self._position = position
        self._hit_box = hit_box
        self._appuye = False

    def getImage(self):
        image = self._image_normale
        if self._appuye :
            image = self._image_appuye
        return image

    def getPosition(self):
        return self._position

    def getEstAppuyer(self):
        return self._appuye

    def appuyer(self):
        self._appuye = True

    def est_clique(self, position_souris:tuple|list):
        est_clique = False
        if position_souris[0] >= self._position[0] and position_souris[0] <= self._position[0]+self._hit_box[0] :
            if position_souris[1] >= self._position[1] and position_souris[1] <= self._position[1]+self._hit_box[1] :
                est_clique = True
        return est_clique

    def nePasAppuyer(self):
        self._appuye = False