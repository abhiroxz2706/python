import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(777,777)
polygon=turtle.Turtle()

num_sides=4
side_length=77
angle=360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()