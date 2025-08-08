import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,500)
polygon=turtle.Turtle()
polygon.width(5)

num_sides=5
side_length=100
angle=144

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()