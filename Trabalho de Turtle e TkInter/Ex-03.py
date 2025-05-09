import turtle
import random

def desenharRetangulos(n):
    turtle.colormode(255)
    t = turtle.Turtle()
    t.pencolor('black')
    t.pensize(2)

    for i in range(n):
        cor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        t.fillcolor(cor)

        t.begin_fill()
        for _ in range(2):
            t.forward(400)
            t.right(90)
            t.forward(40)
            t.right(90)
        t.end_fill()

        t.penup()
        t.left(90)
        t.forward(60)
        t.right(90)
        t.pendown()
        
    turtle.done()

n = int(input("Digite o número de retângulos: "))
desenharRetangulos(n)