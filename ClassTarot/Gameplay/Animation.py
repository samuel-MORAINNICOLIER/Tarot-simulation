import pygame
"""
Définit les animations du jeu
"""
class Animation:
    def __init__(self, frames:list[pygame.Surface], nb_frames:int):
        self._frames = frames
        self._nb_frames = nb_frames

    def get_frame(self, numero):
        """
        Permet d'obtenir la bonne frame
        :param numero: Le numero de la frame
        :return: La surface de la bonne frame ou None si elle n'existe pas
        """
        rep = None
        if numero < self._nb_frames:
            rep = self._frames[numero]
        return rep
