import turtle

def quadrado_cheio(t, x, y, size):
    t.fillcolor("black")
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def desenhar_carpete_recursivo(t, x, y, size, nivel):
    if nivel == 0:
        quadrado_cheio(t, x, y, size)
    else:
        new_size = size / 3
        for dx in range(3):
            for dy in range(3):
                if dx == 1 and dy == 1:
                    continue
                new_x = x + dx * new_size
                new_y = y - dy * new_size
                desenhar_carpete_recursivo(t, new_x, new_y, new_size, nivel - 1)

def desenhar_carpete(nivel):
    tela = turtle.Screen()
    tela.bgcolor("white")
    tela.title("Carpete de Sierpinski - Preto e Branco")

    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(1)
    t.hideturtle()
    
    turtle.tracer(0, 0)  # desliga animação para velocidade

    tamanho_total = 400
    x_inicio = -tamanho_total / 2
    y_inicio = tamanho_total / 2

    desenhar_carpete_recursivo(t, x_inicio, y_inicio, tamanho_total, nivel)

    turtle.update()
    turtle.done()

n = int(input("Digite o nível do Carpete de Sierpinski (0 a 4): "))
desenhar_carpete(n)