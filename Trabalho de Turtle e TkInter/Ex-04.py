import turtle

def desenharTriangulos(n):
    t = turtle.Turtle()
    t.pencolor('black')
    t.pensize(3)

    w = 600
    l = 30
    s = w / (n + 1)

    turtle.penup()
    turtle.hideturtle()
    turtle.goto(w/2 , 0)
    turtle.pendown()

    for _ in range(n):
        t.forward(s)
        t.left(60)
        t.forward(l)
        t.left(240)
        t.forward(l)
        t.left(60)
    t.forward(s)


    turtle.done()


n = int(input("Digite o número de triângulos: "))
desenharTriangulos(n)