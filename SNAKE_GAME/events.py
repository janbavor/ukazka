from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("WELCOME IN SNAKE GAME")

tommy = Turtle()

def move_forward():
    tommy.forward(20)

#Stisknutí klávesy

screen.listen()
screen.onkeypress(move_forward, "w")



screen.exitonclick()