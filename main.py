import random
import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()

# set screen size
screen.setup(width=500, height=400)

# get user's bet choice
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
is_race_on = False
all_turtles = []


def starting_line():
    y_index = -100
    for turtle_index in range(0, len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_index)
        y_index += 30
        all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

starting_line()
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner...")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
