from turtle import Turtle, Screen
import time
import random

# === Definice obrazovky ===

screen = Screen()
screen.colormode(255)
screen.bgcolor(153,204,255)
screen.title("WELCOME IN SNAKE GAME")
screen.setup(width=600, height=600) # je možnost to napsat i (600,600), ale člověk zapomene co to je!
screen.tracer(False) #vypne refreshování stránky!!!! True - zapnuto ale nemusí se psát protože v defaultu je zapnutej, případně 0 - vypnuto, 1 - zapnuto

# === Části hry ===

# Hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0) #vypnutí rychlosti - protože rychlost je nastavená dole v time.sleep
head.penup() #vypnutí tužky - nekreslí žádnou čáru
head.goto(0,0) #souřadnice - výchozí pozice hada
head.direction = "stop" #atribut, který jsme si vytvořili. Kdybych jsem napsal a spustil níže definovanou metodu move(), tak by to jela hlava nahoru pokud by head.direcdtion = "up". Další metody definujou vazby na šipky a rozpohybování.

# Potrava pro hada - jablko
apple = Turtle("circle")
apple.speed(0) #nemusí být, potrava se nehýbe
apple.color("red")
apple.penup() #vypnutí čáry
apple.goto(100,100) # výchozí pozice potravy

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
    if head.direction == "up": #if se dodělalo následně, řeší, aby had nemohl zatáčet např doprava a hned doleva apod. 
        y = head.ycor()
        head.sety(y + 20) # 20 je velikost hlavy - či kostičky hada
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
    if head.direction != "down": #podmínka if se dodělal na konkci, řeší to kolizi např. kliknu nahoru a hned dolu, bez tohoto ifu by to šlo
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
# První v závorce je výše uvedená metoda - funkce, druhá položka je klávesa "Up" = šipka nahoru, mohu napsat cokoliv např s a při zmáčknutí klávesy s to bude reagovat.
screen.listen() # posluchač událostí jako je např. kliknutí na klávesnici. Bez toho to nebude fungovat. 
screen.onkeypress(move_up, "Up") #nemusí se psát závorky, protože se ta funkce nespustí ihned, ale dálě to ta klávesa - jakoby si doplní závorky. 
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")


# === Hlavní cyklus ===

while True:
    screen.update() #udělá update - vytáhne, protože nahoře screen.tracer(False) = celkové vypnutí refreshe, bez tohoto se nic neobjeví, protože nahoře to je vypnuté.
       
    # Kontroal kolize hada s hranou obrazovky (obrazovka 600x600)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2) #2 s pauza a vrátí se na souřadnice
        head.goto(0, 0) 
        head.direction = "stop" #zastavení - spustí se znovu klikem
        # Skryjeme šedé čtverečky - nasbírané potravy hada
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500) # řeknu tímto cyklem for všem čtverečkům in body parts ať jdou mimo plátno
        # Vyprázdníme list s částmi těla - šédé čtverečky, tedy nasbíraná potrava hada
        body_parts.clear() # vyprázdnění se musí udělat, jinak by tam šedé čtverce byly, prtože jede znovu další kód, který je zobrazí, protože vše je ve While
        # Při kolizi se vyčístí skóre a restartuje metoda v Turtle - definované score_sign
        score = 0
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
    
    # Náhodné umístění jablka při kolizi s hadí hlavou a zároveň vytvoření šedého čtverečku - rozšeíření hada za kolizi s potravou    
    if head.distance(apple) < 20: #toto je metoda udělána v Turtle Graphics, 20 máme tu kostičku či jabko. Toto řeší kolizi, tedy když se srazí.
        x = random.randint(-280, 280) #okno máme 600x600 tedy proto 280+-
        y = random.randint(-280, 280)
        apple.goto(x, y) #pokud kolidují tak dej náhodnou pozici jablka
        # Přidání části hada - kostičky se přidaji do seznamu, z kterého ho níže uvedeným cyklem a podmínkou if budeme zoprazovat za hlavou hada.
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("gray")
        new_body_part.penup()
        body_parts.append(new_body_part)
        
        # Zvýšení skóre
        score += 10
        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
    
    # Přidání kostiček za hada - části hada od indexu 1 dál: - vysvětleno v cycle.py, 0 index první kostka za hlavou hada, ji v odstavci níže
    for index in range(len(body_parts)-1, 0, -1): #jde to odzadu a na 0 index to nenojde protože range je do 0, tu nebere, 0index je níže
        x = body_parts[index-1].xcor() # funguje např. 4ku dej na pozici tam kde byla trojka
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x,y)
    
    #nultá část hada
    if len(body_parts) > 0: #když bude v body parts alespoň jeden je splněná podmínka - je to ten nultý
        x = head.xcor() #říká aktuální souřadnici hlavy hada, tedy dává kostičku tam kde byla předtím hlava. 
        y = head.ycor()
        body_parts[0].goto(x, y) # vypadá to opticky, že to skočí za hlavu, protože hlava se furt pohybuje 
        
    move()  # důležité je aby to bylo až tady, díky tomu se hlava pohne dal a část hada zůstane na původní poloze hlavy
   
    
    # Kontrola kolize hada s vlastním tělem 
    # Hlava narazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20: 
            time.sleep(2) 
            head.goto(0, 0) 
            head.direction = "stop" 
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500) 
            body_parts.clear()    
            # Při kolizi se vyčístí skóre
            score = 0
            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
    
    time.sleep(0.1) #0,1 s či nastavený čas počká - pak provede druhý příkaz
    
screen.exitonclick()

# na score by se dala napsat zase funkce