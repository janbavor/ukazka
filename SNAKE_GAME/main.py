from turtle import Turtle, Screen
import time
import random

# === Definice obrazovky ===

screen = Screen()
screen.colormode(255)
screen.bgcolor(153,204,255)
screen.title("WELCOME IN SNAKE GAME")
screen.setup(width=600, height=600) 
screen.tracer(False) 

# === Části hry ===

# Hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0) 
head.penup() 
head.goto(0,0) 
head.direction = "stop" 

# Potrava pro hada - jablko
apple = Turtle("circle")
apple.speed(0) 
apple.color("red")
apple.penup() 
apple.goto(100,100)

# Skóre - udělám to přes objekt - želvu a skryjeme ji a nahradíme číslem
score = 0
highest_score = 0
score_sign = Turtle()
score_sign.speed(0)
score_sign.color("black")
score_sign.penup()
score_sign.hideturtle() #skrytí objektu
score_sign.goto(0, 265)
score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))

# Části těla hada 
body_parts = []

# === FUNKCE ===

# Pohyb hada - definice pohybu po osách x, y
def move():
    if head.direction == "up": 
        y = head.ycor()
        head.sety(y + 20) 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Nápomocén funkce
def move_up():
    if head.direction != "down": 
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_left():
    if head.direction != "right":
        head.direction = "left"
def move_right():
    if head.direction != "left":
        head.direction = "right"

# Kliknutí na klávesy
screen.listen() 
screen.onkeypress(move_up, "Up") 
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")


# === Hlavní cyklus ===

while True:
    screen.update()  
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2) 
        head.goto(0, 0) 
        head.direction = "stop" 
       
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)
       
        body_parts.clear()
        score = 0
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
 
    if head.distance(apple) < 20: 
        x = random.randint(-280, 280) 
        y = random.randint(-280, 280)
        apple.goto(x, y)
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("gray")
        new_body_part.penup()
        body_parts.append(new_body_part)
        
        score += 10
        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
    
    for index in range(len(body_parts)-1, 0, -1): 
        x = body_parts[index-1].xcor() 
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x,y)
    
    if len(body_parts) > 0: 
        x = head.xcor() 
        y = head.ycor()
        body_parts[0].goto(x, y)
   
    move()  
   
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20: 
            time.sleep(2) 
            head.goto(0, 0) 
            head.direction = "stop" 
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500) 
            body_parts.clear() 
            score = 0
            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
    
    time.sleep(0.1) 

screen.exitonclick()
