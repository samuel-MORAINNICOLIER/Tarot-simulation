import pygame
#from PIL import Image


#from ClassTarot.Card import Card
from ClassTarot.Card import MajorArcane
#from ClassTarot.Card import MinorArcane
from ClassTarot.Card import Standard
from ClassTarot.Card import Figure
from ClassTarot.Card import Game
from ClassTarot.Gameplay import Button
from ClassTarot.Gameplay import Animation
from ClassTarot.Gameplay import Message
from ClassTarot.Tirage import TirageActuel
from ClassTarot.Tirage import TiragePossible

# Initialisation de la pile------------------
pile = Game.Game()

# Initialisation des cartes------------------
# Initialisation des cartes mineures :
couleurs = ["baton", "coupe", "ecu", "epee"]
nomFigures = ["valet", "cavalier", "reine", "roi"]

for couleur in couleurs :
    # Initialisation des cartes standards
    for nb in range(1,11):
        card = Standard.Standard(couleur, nb)
        pile.addCard(card)
    # Initialisation des figures
    for nomFigure in nomFigures:
        card = Figure.Figure(couleur, nomFigure)
        pile.addCard(card)

# Test de la pile et du lien des images(validé)
"""
print(pile)
lien = pile.getRandCard().getLienImage()
carte = Image.open(lien)
carte.show()
"""

# Initialisation des tirages possibles------
tirage1 = TiragePossible.TiragePossible("Carte du jour", ["La carte du jour"])
tirage2 = TiragePossible.TiragePossible("Tirage en 2 cartes", ["Le pour", "Le contre"])
tirage3 = TiragePossible.TiragePossible("Tirage en 3 cartes", ["Le Passé", "Le Présent", "Le Future"])
tirage4 = TiragePossible.TiragePossible("Tirage en 4 carte", ["L'eau", "l'air", "Le feu", "La terre"])
#tirage5 = TiragePossible.TiragePossible("Tirage en 5 carte", ["Le pour", "Le contre", "la vibration", "La synthèse"])

# Initialisation du tirage actuel-----------
divination = TirageActuel.TirageActuel()
divination.addTiragePossibles(tirage1)
divination.addTiragePossibles(tirage2)
divination.addTiragePossibles(tirage3)
divination.addTiragePossibles(tirage4)
#divination.addTiragePossibles(tirage5)

# Partie------------------------------------

resolution = 8
WIDTH = 190*resolution # Largeur
HEIGHT = 108*resolution # Hauteur

pygame.display.set_caption("Simulateur de Tarot") # Nom de la fenêtre
screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # Création de la fenêtre

# Liens
backgroundLien = "Images/table.png"
cardBackLien = "Images/Cards/cardBack.png"
pileLien = "Images/cards/pileBack.png"
melangerNormaleLien = "Images/Gameplay/buttonMelangerNormale.png"
melangerAppuyerLien = "Images/Gameplay/buttonMelangerAppuyer.png"
couperNormaleLien = "Images/Gameplay/buttonCouperNormale.png"
couperAppuyerLien = "Images/Gameplay/buttonCouperAppuyer.png"
tirerNormaleLien = "Images/Gameplay/buttonTirerNormale.png"
tirerAppuyerLien = "Images/Gameplay/buttonTirerAppuyer.png"
retournerNormaleLien = "Images/Gameplay/buttonRetournerNormale.png"
retournerAppuyerLien = "Images/Gameplay/buttonRetournerAppuyer.png"
recommencerLien = "Images/Gameplay/buttonRecomencerNormale.png"
quitterLien = "Images/Gameplay/buttonQuitterNormale.png"

# Images
background = pygame.image.load(backgroundLien)
cardBack = pygame.image.load(cardBackLien)
pileBack = pygame.image.load(pileLien)
melangerNormale = pygame.image.load(melangerNormaleLien)
melangerAppuyer = pygame.image.load(melangerAppuyerLien)
couperNormale = pygame.image.load(couperNormaleLien)
couperAppuyer = pygame.image.load(couperAppuyerLien)
tirerNormale = pygame.image.load(tirerNormaleLien)
tirerAppuyer = pygame.image.load(tirerAppuyerLien)
retournerNormale = pygame.image.load(retournerNormaleLien)
retournerAppuyer = pygame.image.load(retournerAppuyerLien)
recommencer = pygame.image.load(recommencerLien)
quitter = pygame.image.load(quitterLien)

# Position
position_background  = [0,0]
position_pile = [-330,90]
position_carte_tire = [WIDTH/2-600,HEIGHT/2+65]
position_description = [600,80]

# position boutons
position_Melanger = [370,70]
position_couper = [370,170]
position_tirer = [401, 270]
position_retourner = [610,270]
position_recommencer = [900,-30]
position_quitter = [1200,-30]


# Redimensions images
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
cardBack = pygame.transform.scale(cardBack, (140*1.5,240*1.5))
pileBack = pygame.transform.scale(pileBack, (285*2.5,157.5*2.5))
melangerNormale = pygame.transform.scale(melangerNormale, (240,140))
melangerAppuyer = pygame.transform.scale(melangerAppuyer, (240,140))
couperNormale = pygame.transform.scale(couperNormale,(240,140))
couperAppuyer = pygame.transform.scale(couperAppuyer,(240,140))
tirerNormale = pygame.transform.scale(tirerNormale, (240,140))
tirerAppuyer = pygame.transform.scale(tirerAppuyer, (240,140))
retournerNormale = pygame.transform.scale(retournerNormale, (280,140))
retournerAppuyer = pygame.transform.scale(retournerAppuyer, (280,140))
recommencer = pygame.transform.scale(recommencer, (280,140))
quitter = pygame.transform.scale(quitter, (280,140))


# Initialisation des éléments de gameplay---
# Initialisation des boutons
melanger = Button.Button(melangerNormale,melangerAppuyer, position_Melanger,(240, 140))
couper = Button.Button(couperNormale, couperAppuyer, position_couper, (240, 140))
tirer = Button.Button(tirerNormale, tirerAppuyer, position_tirer, (240, 140))
retourner = Button.Button(retournerNormale, retournerAppuyer, position_retourner, (280, 140))
recommencer = Button.Button(recommencer,recommencer, position_recommencer, (280,140))
quitter = Button.Button(quitter, quitter, position_quitter, (280,140))

# Initialisation des messages
# Initialisation de la description
message_description = Message.Message(["Divination"],(255,255,255),24, position_description)

# Initialisation des animations
coupe_frames = []
for i in range(0,15):
    frameLien = "Images/animation/coupe/pixil-frame-"+str(i)+".png"
    frame = pygame.image.load(frameLien)
    frame = pygame.transform.scale(frame, (285*2.5,157.5*2.5))
    coupe_frames.append(frame)
animation_coupe = Animation.Animation(coupe_frames,len(coupe_frames))

mix_frames = []
for i in range(0,21):
    frameLien = "Images/animation/mix/pixil-frame-"+str(i)+".png"
    frame = pygame.image.load(frameLien)
    frame = pygame.transform.scale(frame, (285*2.5,157.5*2.5))
    mix_frames.append(frame)
animation_mix = Animation.Animation(mix_frames,len(mix_frames))

# Initialisation des compteurs
# Initialisation des compteurs de boutons
comp_melanger = None
comp_couper = None
comp_tirer = None
comp_retourner = None
comp_anim_coup = None
comp_anim_melange = None

# variable générale
# Temps d'attente de tous les compteurs :
temps_attente = 2

# Est-ce que la pile bouge ?
pile_mouvement = False

# Couleur du fond
background_color = "purple"

def menu():
    main_game()

def main_game():
    global pile, comp_melanger, comp_couper, comp_tirer, comp_anim_coup
    global comp_anim_melange,comp_retourner, temps_attente, pile_mouvement
    global message_description
    clock = pygame.time.Clock()
    FPS = 60
    play=True
    pygame.mixer.init()

    pygame.display.update()
    while play:

        # FPS frames par secondes
        clock.tick(FPS)

        # gérer les évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            if melanger.est_clique(pygame.mouse.get_pos()):
                melanger.appuyer()
                comp_melanger = temps_attente
                if not pile_mouvement:
                    pile.mixPile()
                    # Animation pour melanger
                    comp_anim_melange = 21
                    pile_mouvement = True
            if couper.est_clique(pygame.mouse.get_pos()):
                couper.appuyer()
                comp_couper = temps_attente
                if not pile_mouvement :
                    pile.couperPile(len(pile.getPile())//2)
                    comp_anim_coup = 15
                    pile_mouvement = True
            if tirer.est_clique(pygame.mouse.get_pos()):
                tirer.appuyer()
                comp_tirer = temps_attente
                if len(divination.getCardTire()) < len(divination.getTiragePossibles()):
                    divination.piocherDepuisRand(pile)
                    msg =["Divination : "]
                    for msg_carte in divination.DireLAventure():
                        msg.append(msg_carte[0]+"  =>  "+msg_carte[1])
                    message_description.setMessage(msg)
            if retourner.est_clique(pygame.mouse.get_pos()):
                retourner.appuyer()
                comp_retourner = temps_attente
                if 0 < len(divination.getCardTire()):
                    divination.retourneCard()
            if recommencer.est_clique(pygame.mouse.get_pos()):
                recommencer.appuyer()
                play = False
            if quitter.est_clique(pygame.mouse.get_pos()):
                quitter.appuyer()
                play = False

        # Vérifier les compteurs
        # Vérifier les compteurs de boutons
        if comp_melanger is not None :
            if comp_melanger <= 0:
                comp_melanger = None
                melanger.nePasAppuyer()
        if comp_couper is not None :
            if comp_couper <= 0:
                comp_couper = None
                couper.nePasAppuyer()
        if comp_tirer is not None :
            if comp_tirer <= 0:
                comp_tirer = None
                tirer.nePasAppuyer()
        if comp_retourner is not None :
            if comp_retourner <= 0:
                comp_retourner = None
                retourner.nePasAppuyer()

        # Vérifier les compteurs des animations
        if comp_anim_coup is not None:
            if comp_anim_coup <= 1:
                comp_anim_coup = None
                pile_mouvement = False
        if comp_anim_melange is not None:
            if comp_anim_melange <= 1:
                comp_anim_melange = None
                pile_mouvement = False

        # Décrémenter les compteurs s'ils en ont besoin
        if comp_melanger is not None :
            comp_melanger -=1
        if comp_couper is not None :
            comp_couper -=1
        if comp_tirer is not None :
            comp_tirer -=1
        if comp_retourner is not None :
            comp_retourner -=1
        if comp_anim_coup is not None:
            comp_anim_coup -=1
        if comp_anim_melange is not None:
            comp_anim_melange -=1

        # 1. Déplacer les objets

        # 2. Effacer la surface
        # Mettre en place le fond d'écran
        # screen.blit(background, position_background)  # On recharge l'image
        screen.fill(background_color)

        # 3. Afficher les objets
        # Affichage de la pile
        if not pile_mouvement :
            screen.blit(pileBack, position_pile)
        if comp_anim_coup is not None :
            screen.blit(animation_coupe.get_frame(15-comp_anim_coup), position_pile)
        if comp_anim_melange is not None :
            screen.blit(animation_mix.get_frame(21-comp_anim_melange), position_pile)

        # Affichage des boutons
        screen.blit(melanger.getImage(), position_Melanger)
        screen.blit(couper.getImage(), position_couper)
        screen.blit(tirer.getImage(), position_tirer)
        screen.blit(retourner.getImage(), position_retourner)
        screen.blit(recommencer.getImage(), position_recommencer)
        screen.blit(quitter.getImage(), position_quitter)

        # Affichage du tirage divinatoire
        for i_carteTire in range(len(divination.getCardTire())):
            if not divination.getRetourne():
                screen.blit(cardBack, (position_carte_tire[0]+220*i_carteTire, position_carte_tire[1]))
                # A améliorer
            elif divination.getRetourne():
                image_card = pygame.image.load(divination.getCardTire()[i_carteTire].getLienImage())
                image_card = pygame.transform.scale(image_card, (140*1.5,240*1.5))
                screen.blit(image_card, (position_carte_tire[0] + 220 * i_carteTire, position_carte_tire[1]))

        # Affichage du message divinatoire
        if divination.getRetourne() :
            message_description.afficheMessage(screen)

        # Exécuter un temps de pause :
        pygame.time.wait(60)

        # Basculer le buffer screen sur l'écran
        pygame.display.flip()
    return

menu()