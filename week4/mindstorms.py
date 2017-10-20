import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.color("red")
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    brad.color("white")
    brad.circle(100)

    window.exitonclick()

draw_square()
