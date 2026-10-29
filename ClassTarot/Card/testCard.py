import Card
import MajorArcane
import Standard
import Figure
import Game

carte1 = Card.Card()
print(carte1.getDescription())
print(carte1)

hermite = MajorArcane.MajorArcane(9, "l'hermite")
print(hermite)

hermite.setDescriptionSuite(" et est une carte très intéressante.")

print(hermite)


roi_baton = Figure.Figure("Baton", "Roi")
print(roi_baton)

quatre_baton = Standard.Standard("Baton", 4)
print(quatre_baton)

jeu1 = Game.Game()
print(jeu1)

jeu1.addCard(hermite)
jeu1.addCard(roi_baton)
jeu1.addCard(quatre_baton)

print("Premier élément du jeu1 : ")
print(jeu1.getPile()[0])

print(jeu1)
print("Mélange de la pile")
jeu1.mixPile()
print(jeu1)

print(jeu1.couperPile(1))
print(jeu1)