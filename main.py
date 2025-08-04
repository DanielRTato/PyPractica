from turtle import Turtle, Screen
import  random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

for tutle_i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[tutle_i])
    new_turtle.goto(x=-230, y=y_position[tutle_i])
    all_turtles.append(new_turtle)

# Screen size and picking tortle
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the rece? Enter a color: ")
print(user_bet) # for testingg

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You`ve won! The {winning_color} turtle is the winer!")
            else:
                print(f"You`ve lost! The {winning_color} turtle is the winer!")



        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# drawing a square
#for _ in range(4):
#    tortuga.forward(100)
#    tortuga.left(90)

#tortuga.clear()

#def draw_spahe(num_sides):
#    angle = 360 / num_sides
#   for _ in range (num_sides):
# #     tortuga.forward(100)
#      tortuga.right(angle)

#for shape_side_n in range(3,11):
#   draw_spahe(shape_side_n)



screen.exitonclick()

