import turtle
import time
from random import randint


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


# holds body
segments = []
DELAY = 0.15
SCORE = 0
HIGH_SCORE = 0

# basic board
win = turtle.Screen()
win.title("Shimmy's game")
win.bgcolor("blue")
win.setup(width=1100, height=1100)
win.tracer(0)
# snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"
# setup keyboard
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
# setup food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("green")
food.penup()
food.shapesize(1.70, 1.70)
food.goto(0, 1)
# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}"
          .format(HIGH_SCORE), align="center", font=("Courier", 24, "normal"))

# game loop
while True:
    win.update()
    move()
    # setup eating
    if head.distance(food) < 15:
        x = randint(-290, 290)
        y = randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        SCORE = SCORE + 10
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
        pen.clear()
        pen.write("score: {} High Score: {}"
                  .format(SCORE, HIGH_SCORE), align="center", font=("Courier", 24, "normal"))
    if head.xcor() > 640 or head.xcor() < -640 or head.ycor() > 640 or head.ycor() < -640:
        segments = []
        head.goto(0, 0)
        SCORE = 0

        # update score
        pen.clear()
        pen.write("score: {} High Score: {}".format(SCORE, HIGH_SCORE), align="center", font=("Courier", 24, "normal"))

        head.direction = "stop"
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # fix first body
    if len(segments) > 0:
        x = head.xcor() + 1
        y = head.ycor() + 1
        segments[0].goto(x, y)

    time.sleep(DELAY)
