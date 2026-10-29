from ClassTarot.Card import Card, Game, MajorArcane
from ClassTarot.Tirage import TiragePossible, TirageActuel

#from ClassTarot.Card import Card

Pile = Game.Game()
for i in range(5):
    Pile.addCard(Card.Card(" dont le n° est le "+str(i)+"."))
hermite = MajorArcane.MajorArcane(9, "l'hermite")
Pile.addCard(hermite)

tirage1 = TiragePossible.TiragePossible("Carte du jour", ["La carte du jour"])
tirage2 = TiragePossible.TiragePossible("Tirage en 2 cartes", ["Le pour", "Le contre"])
tirage3 = TiragePossible.TiragePossible("Tirage en 3 cartes", ["Le Passé", "Le Présent", "Le Future"])

tirageCartes = TirageActuel.TirageActuel()
tirageCartes.addTiragePossibles(tirage1)
tirageCartes.addTiragePossibles(tirage2)
tirageCartes.addTiragePossibles(tirage3)


print(tirage1)
print(tirage2)
print(tirage3)
print(Pile)

tirageCartes.piocherDepuisRand(Pile)
tirageCartes.piocherDepuisRand(Pile)
tirageCartes.piocherDepuisRand(Pile)
print(tirageCartes)
print(Pile)

print("La bonne aventure : \n")
for carteRole,carteDesc in tirageCartes.DireLAventure():
    print(str(carteRole)+" : "+ str(carteDesc))
