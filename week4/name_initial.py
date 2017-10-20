import turtle

def draw_k(t, start_x, start_y):
    
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.setheading(90)
    t.forward(50)
    t.goto(start_x, start_y)
    t.setheading(270)
    t.forward(50)
    t.goto(start_x, start_y)
    t.setheading(45)
    t.forward(75)
    t.goto(start_x, start_y)
    t.setheading(315)
    t.forward(75)
    
def draw_l(t, start_x, start_y):
    
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.setheading(90)
    t.forward(50)
    t.setheading(270)
    t.forward(100)
    t.setheading(0)
    t.forward(75)
    
    
def draw_initial():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    draw_k(t, 0, 0)
    draw_l(t, 100, 0)
    window.exitonclick()
    
draw_initial()
