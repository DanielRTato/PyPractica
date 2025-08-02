from turtle import Turtle, Screen

tortuga= Turtle()
tortuga.shape("turtle")
tortuga.color("red")

# drawing a square
#for _ in range(4):
#    tortuga.forward(100)
#    tortuga.left(90)

#tortuga.clear()

def draw_spahe(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        tortuga.forward(100)
        tortuga.right(angle)

for shape_side_n in range(3,11):
    draw_spahe(shape_side_n)















screen = Screen()
screen.exitonclick()

