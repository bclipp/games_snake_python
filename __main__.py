import turtle
import time
from random import random


def move():
    if head.direction == "up":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


win = turtle.Screen()
win.title("Kalgi's snake game")
win.bgcolor("blue")
win.setup(width=600, height=600)
win.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"
delay=0.1
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)
if head.distance(food) <15:
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)
segments = []
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)
for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

for segment in segments:
    segment.goto(1000, 1000)

segments = []

for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segment list
        segment.clear()
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
high_score  = 100
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
score = 0
high_score = 0
score = score + 10

if score > high_score:
    high_score = score

while True:
    win.update()
    move()
    time.sleep(delay)
