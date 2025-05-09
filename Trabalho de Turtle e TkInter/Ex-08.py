import tkinter as tk
import random

def corAleatoria():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def T():
    window = tk.Tk()
    window.title("Desenho das Regiões")
    window.geometry("800x800")

    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    x1, y1 = t + 100, 200
    reta1 = [
        x1, y1,
        x1 + 2 * t, y1,
    ]

    x2,y2 = x1 + t , 200 - t
    reta2= [
        x2 , y2,
        x2 , y2 + 2 * t,
    ]

    x3, y3 = (x1 + t) + (t * 0.1) , (y2 + t) + (t * 0.1)
    quadrado = [
        x3, y3,
        x3 + (0.9 * t) , y3, 
        x3 + (0.9 * t) , y3 + (0.9 * t),
        x3, y3 + (0.9 * t),
    ]   

    x4, y4 = (x1 + t) + (t * 0.1) , y3 - (2 * (t * 0.1))
    triangulo = [
        x4, y4,
        x4 + (0.9 * t) , y4,
        x4 + (0.9 * t) / 2 , y4 - (0.9 * t),
    ]

    canvas.create_polygon(reta1, outline='black')
    canvas.create_polygon(reta2, outline='black')
    canvas.create_polygon(quadrado, outline='black' , fill = corAleatoria())
    canvas.create_polygon(triangulo, outline='black' , fill = corAleatoria())
    canvas.create_oval(x1 , y2 + t + (0.1 * t) , x1 + t - (0.1 * t) , y2 + t + (0.1 * t) + 2 * (0.45 * t) , outline = 'black', width = 1 , fill = corAleatoria())

    window.mainloop()

t = int(input("Informe o número de T: "))
T()