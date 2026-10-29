import pygame
pygame.font.init()
"""
Définit les messages pouvant apparaitre dans le jeu
"""
class Message :
    def __init__(self, msg:list[str], color_msg:str|tuple|list, taille, position:list):
        """
        Définit un message
        :param msg: tableau des lignes du message
        :param color_msg:
        :param taille:
        :param position:
        """
        self._msg:list[str] = msg
        self._color_msg = color_msg
        self._taille = taille
        self._position = position
        self._police = pygame.font.Font("Minecraftia-Regular.ttf", self._taille)

    def getMessage(self):
        return self._msg

    def getPosition(self):
        return self._position

    def afficheMessage(self, screen):
        """

        :param screen: Surface de pygame / écran principale
        :return: none
        """
        position = []
        position += self._position
        for ligne in self._msg:
            rendu_ligne = self._police.render(ligne, True, self._color_msg)
            screen.blit(rendu_ligne, position)
            position[1]+=self._taille+8

    def setMessage(self, msg:list[str]):
        self._msg = msg