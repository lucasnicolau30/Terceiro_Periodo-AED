import tkinter as tk

def desenhar_triangulos():
    window = tk.Tk()
    window.title("Triângulos com Tkinter")
    window.geometry("800x600")

    canvas = tk.Canvas(window, width=800, height=600, bg='#D3D3D3')
    canvas.pack()

    x1, y1 = 150, 200
    triangulo1 = [
        x1, y1,
        x1 + 150, y1,
        x1 + 150/2, y1 + 120
    ]

    x2, y2 = x1 + 100 , y1 + 120
    triangulo2 = [
        x2, y2,
        x2 + 150 , y2,
        x2 + 75 , y2 - 120
    ]

    x3, y3 = x2 + 100 , 200
    triangulo3 = [
        x3, y3,
        x3 + 150 , y3,
        x3 + 150/2 , y3 + 120
    ]    

    canvas.create_polygon(triangulo1, outline='black', fill='red')
    canvas.create_polygon(triangulo2, outline='black', fill='green')
    canvas.create_polygon(triangulo3, outline='black', fill='blue')

    window.mainloop()

desenhar_triangulos()