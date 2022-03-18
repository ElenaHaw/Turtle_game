# Turtle game, a game about a hungry turtle 

import turtle
import math
import random
import winsound
import time



# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
wn.bgpic('underwater.gif')
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('lime')
player.shape('turtle')
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()

# Create timer zone
mypen3 = turtle.Turtle()
mypen3.color('green')
mypen3.hideturtle()


# Create variable score
score = 0
comp_score = 0


#Create food
maxFoods = 50
foods = []
for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(1)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

# Set speed variable
speed = 1

# Set game time limit for 25 seconds 
timeout = time.time() + 5*5
start_time=time.time()

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 2

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left,'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

while True:
    gametime = 0
    if time.time() >= timeout:
        
        while True:
          
            if (int(score) > int(comp_score)):
                mypen.setposition(0, 0)
                mypen.color("yellow")
                mypen.write("The game is over: You WIN", False, align="center", font=("Arial", 28, "normal"))
            else:
                mypen.setposition(0, 0)
                mypen.color("yellow")
                mypen.write("The game is over: You LOOSE", False, align="center", font=("Arial", 28, "normal"))     
        
        break
    gametime = gametime - 1
    
    player.forward(speed)
    comp.forward(10)

    # Boundary Comp Checking x coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
        comp.right(random.randint(30,155))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    # Boundary Comp Checking y coordinate
    if comp.ycor() > 290 or comp.ycor() < -290:
        comp.right(random.randint(30,155))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    
    # Move food around
    for food in foods:
        
        # Draw the timer on the screen
        mypen3.undo()
        mypen3.penup()
        mypen3.hideturtle()
        mypen3.setposition(-20, 302)
        elapsed_time=time.time()-start_time
        timelimit=25
        timer=timelimit-elapsed_time
        timerstring ="Time: %s" % int(timer)
        mypen3.write(timerstring, False, align='left', font=('Arial', 14, 'normal'))


        food.shapesize(.5)
        food.forward(3)
        
        # Boundary food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        # Boundary food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)  


        # Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            score +=1
            winsound.PlaySound('chomp.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-300, 305)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        # Comp Collision checking
        if isCollision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0,360))
            comp_score+=1
            winsound.PlaySound('chomp.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            # Draw the Comp score on the screen
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % comp_score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
       
    