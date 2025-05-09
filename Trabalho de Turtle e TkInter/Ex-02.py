import turtle 

def desenharRetangulos():
    turtle.colormode(255) 
    t = turtle.Turtle()
    t.pencolor('black') 
    t.pensize(2)

    t.fillcolor(144, 238, 144)       
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()

    t.up()
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pd()

    t.fillcolor(137, 207, 240)        
    t.begin_fill()
    for _ in range(1):
        t.forward(400)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(400)
        t.right(90)
        t.forward(40)
    t.end_fill()

    turtle.done()

desenharRetangulos()