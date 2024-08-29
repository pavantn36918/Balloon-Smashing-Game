import turtle
import math
import random
import pygame

# Initialize pygame
pygame.init()

# Load and play background music
pygame.mixer.music.load(r"C:\Users\narasimhaiah\Desktop\pavan\Pavan\cg mini project\CG MINI PROJECT\bgmusic.mp3")  # Replace with your music file path
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
pygame.mixer.music.set_volume(0.5)
# Load collision sound effect
collision_sound = pygame.mixer.Sound(r"C:\Users\narasimhaiah\Desktop\pavan\Pavan\cg mini project\CG MINI PROJECT\blast.wav")  # Replace with your collision sound file path
collision_sound.set_volume(1.0)

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("green")
wn.tracer(2)
#wn.bgpic(r"C:\Users\narasimhaiah\Desktop\pavan\Pavan\cg mini project\CG MINI PROJECT\kbgame.jpg")

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-350, -300)
mypen.pendown()
mypen.pensize(3)

for side in range(2):
    mypen.forward(694)
    mypen.left(90)
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# Create goals
maxgoals = 10
goals = []

for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-350, 330), random.randint(-300, 300))

# Set speed variable
speed = 1

# Initialize score
score = 0

# Initialize lives
lives = 3

# Create score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.setposition(-340, 260)
score_display.hideturtle()
score_display.write("Score: {}".format(score), align="left", font=("Arial", 14, "normal"))

# Create lives display
lives_display = turtle.Turtle()
lives_display.speed(0)
lives_display.color("white")
lives_display.penup()
lives_display.setposition(200, 260)
lives_display.hideturtle()
lives_display.write("Lives: {}".format(lives), align="left", font=("Arial", 14, "normal"))

# Define the functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return d < 20

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write("Score: {}".format(score), align="left", font=("Arial", 14, "normal"))

def lose_life():
    global lives
    lives -= 1
    lives_display.clear()
    lives_display.write("Lives: {}".format(lives), align="left", font=("Arial", 14, "normal"))
    if lives == 0:
        game_over()

def game_over():
    player.hideturtle()
    for goal in goals:
        goal.hideturtle()
    game_over_display = turtle.Turtle()
    game_over_display.speed(0)
    game_over_display.color("white")
    game_over_display.penup()
    game_over_display.setposition(0, 0)
    game_over_display.hideturtle()
    game_over_display.write("GAME OVER", align="center", font=("Arial", 36, "normal"))
    wn.update()
    pygame.mixer.music.stop()
    turtle.done()

# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")

# Main game loop
while True:
    player.forward(speed)

    # Checking boundary
    if player.xcor() > 330 or player.xcor() < -350:
        player.right(100)
        lose_life()

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(100)
        lose_life()

    # Move the goals
    for count in range(maxgoals):
        goals[count].forward(3)

        # Checking boundary
        if goals[count].xcor() > 330 or goals[count].xcor() < -340:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            
        if isCollision(player, goals[count]):
            collision_sound.play()
            goals[count].setposition(random.randint(-350, 330), random.randint(-300, 300))
            goals[count].right(random.randint(0, 300))
            update_score()

wn.mainloop()
