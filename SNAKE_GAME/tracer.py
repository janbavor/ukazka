# testovací soubor - vysvětlení traceru!

from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("WELCOME IN SNAKE GAME")
screen.setup(width=600, height=600)
screen.tracer(False) #pokud toto vypnu je to ok, vypnu neustálé refreshování - nutno zobrazit screen.update() - tím řídím načteni stránky! viz níže.

square1 = Turtle("square")
square2 = Turtle("square")
square1.penup()
square1.goto(0,0)
square2.penup() # pokud by to nebylo, dělalo by to čáru
square2.goto(-20, 0)

for _ in range(80):
    square1.forward(10)
    square2.forward(10)
    time.sleep(0.1) #nutno naimportovat modul time
    screen.update() #řízení načtení stránky

screen.exitonclick()