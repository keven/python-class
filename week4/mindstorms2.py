import turtle

def draw_square(t):
    for i in range(0,4):
        t.forward(100)
        t.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.color("red")
    for i in range(0, 36):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()
