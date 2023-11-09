from turtle import Turtle, Screen
import time
import random

# Variables
score = 0
highest_score = 0

screen = Screen()
screen.bgcolor("green")
screen.title("Welcome to Snake Game")
screen.setup(width = 600, height = 600)
screen.tracer(False)

# Snake's head
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# apple
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

# score
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Score: 0  Highest score: 0", align="center", font=("Arial", 18))


# body parts
body_parts = []

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

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

# pressing the keys
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# Main cycle
while True:
    screen.update()

    # Check colision with the edge of canvas
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the body parts
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)
        
        # Clear the list with body parts(grey squares)
        body_parts.clear()

        # Reset score
        score = 0

        score_sign.clear()
        score_sign.write(f"Score: {score}  Highest score: {highest_score}", align="center", font=("Arial", 18))


    # Head colides with apple - snake eats food
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)
        

        # Adding body parts
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        # increase score
        score += 10

        if score > highest_score:
            highest_score = score
        
        score_sign.clear()
        score_sign.write(f"Score: {score}  Highest score: {highest_score}", align="center", font=("Arial", 18))

    # The last square is glued behind the last square so far
    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)

    # Zero square is glued directly behind the head  
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()

    # head colides with body
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the body parts
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)
        
            # Clear the list with body parts(grey squares)
            body_parts.clear()

            # Reset score
            score = 0
            
            score_sign.clear()
            score_sign.write(f"Score: {score}  Highest score: {highest_score}", align="center", font=("Arial", 18))

    time.sleep(0.1)
    
screen.exitonclick()