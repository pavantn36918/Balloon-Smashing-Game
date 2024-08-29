import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("green")
wn.tracer(1.9)
#wn.bgpic("")

#draw border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-350,-300)
mypen.pendown()
mypen.pensize(3)

for side in range(2):
    mypen.forward(694)
    mypen.left(90)
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


#create player turtle

player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#create goals
maxgoals=6
goals=[]

for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-350,330), random.randint(-300,300))





#set speed variable
speed=1


#definig the functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed+=1

def isCollision(t1, t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)  + math.pow(t1.ycor()-t2.ycor(),2))

    if d<20:
        return True
    else:
        return False


#set kwyboard bindings

turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")


while True:
    player.forward(speed)

    #checking boundray
    if player.xcor()>330 or player.xcor() < -350:
        player.right(100)

    if player.ycor()>300 or player.ycor() < -300:
        player.right(100)

    #collision checking
  
        

    #Move the goal
    for count in range(maxgoals):
        goals[count].forward(3)


        #checking boundray
        if goals[count].xcor()>330 or goals[count].xcor() < -340:
            goals[count].right(180)

        if goals[count].ycor()>290 or goals[count].ycor() < -290:
            goals[count].right(180)
            
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-350,330), random.randint(-300,300))
            goals[count].right(random.randint(0,300))













delay=input("Press Enter to finish.")





