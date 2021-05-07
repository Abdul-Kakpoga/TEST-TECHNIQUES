import turtle
from tkinter import *
from turtle import *

#les fonctions en foction des tailles
def etoile0():
    print("Rien à afficher !!")


def etoile1():
    for i in range(6):
        for j in range(3):
            up()
            turtle.write("*")
            forward(1)
            up()
            #turtle.write("*")
            forward(2)
            up()
        right(120)
        for j in range(3):
            up()
            turtle.write("*")
            forward(1)
            up()
            #turtle.write("*")
            forward(2)
        left(60)


def etoile2():
    for i in range(6):
        for j in range(5):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        right(120)
        for j in range(5):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        left(60)


def etoile3():
    for i in range(6):
        for j in range(7):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        right(120)
        for j in range(7):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        left(60)


def etoile4():
    for i in range(6):
        for j in range(8):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        right(120)
        for j in range(8):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        left(60)


def etoile5():
    for i in range(6):
        for j in range(10):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        right(120)
        for j in range(10):
            up()
            turtle.write("*")
            forward(5)
            up()
            turtle.write("*")
            forward(5)
        left(60)


#Saisie de l'utilisateur d'une valeur entre l'intervalle donné
taille = int(input("entrez une valeur de 0 a 5 "))

#Affichage des étoiles selon la taille saisie par l'utilisateur
if taille == 0:
    print(etoile0())

elif taille == 1:
    print(etoile1())

elif taille == 2:
    print(etoile2())

elif taille == 3:
    print(etoile3())

elif taille == 4:
    print(etoile4())

elif taille == 5:
    print(etoile5())


mainloop()