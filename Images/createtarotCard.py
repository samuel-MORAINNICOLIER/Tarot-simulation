from PIL import Image
"""
cadre = Image.open('cadre.png')
carreau = Image.open('carreau.png')
un = Image.open('1.png')

card = Image.new("RGBA", (1400,2400))

signe_h = (300,-500)
signe_b = (-300,1000)

nb_h = (-300,-500)
#nb_b

card.paste(cadre)
card.paste(carreau,signe_h,carreau)
card.paste(carreau,signe_b,carreau)
card.paste(un,nb_h,un)

card.show()
"""
#cadre = cadre.resize((70,140))
#cadre.save('card1.png')

#signe.rotate(180).show()
#nom = "ImageSigne/"+str(1)+".png"
#Image.open("ImageSigne/"+str(1)+".png").show()


cadre = Image.open('ImageSigne/cadre.png')

heart = Image.open('ImageSigne/heart.png')
trefle = Image.open('ImageSigne/trefle.png')
pique = Image.open('ImageSigne/pique.png')
carreau = Image.open('ImageSigne/carreau.png')

coupe = Image.open('ImageSigne/coupe.png')
ecu = Image.open('ImageSigne/bouclier.png')
epee = Image.open('ImageSigne/epee.png')
baton = Image.open('ImageSigne/baton.png')

signe = carreau
#symbole = trefle
repertoire = "baton"

# Pour les figures :
for figure in ["roi","reine","cavalier","valet"]:
    card = Image.new("RGBA", (1400, 2800))
    # Ajout du cadre
    card.paste(cadre)
    # Ajout du signe
    card.paste(signe, None, signe)
    card.paste(signe.rotate(180), None, signe.rotate(180))
    # Ajout du symbole de la figure
    symb_figure = Image.open("ImageSigne/"+str(figure)+".png")
    card.paste(symb_figure, None, symb_figure)
    card.save("Cards/" + str(repertoire) + "/" + str(repertoire) + str(figure) + ".png")

# Pour les cartes mineure de 1 à 10
"""
for nb in range(1,11):
    card = Image.new("RGBA", (1400, 2800))
    # Ajout du cadre
    card.paste(cadre)
    # Ajout du signe
    card.paste(signe, None, signe)
    card.paste(signe.rotate(180), None, signe.rotate(180))
    # Ajout du nombre
    nombre = Image.open("ImageSigne/"+str(nb)+".png")
    card.paste(nombre, None, nombre)
    card.paste(nombre.rotate(180), None, nombre.rotate(180))
    # Ajout du symbole
    card.paste(symbole, None, symbole)
    card.save("Cards/"+str(repertoire)+"/"+str(repertoire)+str(nb)+".png")
"""