import turtle

def desenharTriangulo():
    t = turtle.Turtle()
    t.color('black')
    t.pensize(1)

    t.fillcolor('pink')
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(120)
    t.forward(150)    
        
    t.end_fill()
    turtle.done()

desenharTriangulo()