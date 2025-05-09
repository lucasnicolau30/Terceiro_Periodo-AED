import turtle

def desenharTriangulos():
    t = turtle.Turtle()
    t.color('black')
    t.pensize(1)

    t.penup()
    t.goto(-300, 300)
    t.pendown()

    t.fillcolor('red')
    t.begin_fill()

    t.forward(150)
    t.right(180 - 58) # ângulo encontrado a partir da lei dos cossenos
    t.forward(141.5)
    t.right(180 - 64) # ângulo encontrado a partir da lei dos cossenos
    t.forward(141.5)

    t.end_fill()
    t.hideturtle() 

    t.color('black')
    t.pensize(1)

    t.penup()
    t.goto(-120 + 75, 180) # -120 pois se dá pela soma de -300 + 150 (base) + 30 (espaçamento) + 75 pela metade da base ; ja o 300 - 120 do y se deve pela altura do triângulo
    t.pendown()

    t.fillcolor('green')
    t.begin_fill()
    t.hideturtle()
    
    t.forward(141.5)
    t.left(180 - 64) # ângulo encontrado a partir da lei dos cossenos
    t.forward(141.5)
    t.left(180 - 58) # ângulo encontrado a partir da lei dos cossenos
    t.forward(150)
    
    t.end_fill()

    t = turtle.Turtle()
    t.color('black')
    t.pensize(1)

    t.penup()
    t.goto(-90, 300)  # -90 pois se dá pela soma de -300 + 150 (base) + 60 (30 * 2 dos espaçamentos);
    t.pendown()

    t.fillcolor('blue')
    t.begin_fill()

    t.forward(150)
    t.right(180 - 58) # ângulo encontrado a partir da lei dos cossenos
    t.forward(141.5)
    t.right(180 - 64) # ângulo encontrado a partir da lei dos cossenos
    t.forward(141.5)

    t.end_fill()
    t.hideturtle()

desenharTriangulos()

turtle.done()