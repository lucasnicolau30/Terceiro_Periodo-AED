import tkinter as tk

def olimpiadas():
    window = tk.Tk()
    window.title("Símbolo das Olimpíadas")
    window.geometry("800x600")

    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    canvas.create_oval(85 ,20 , 285 , 220 , outline = '#0885c2', width = 5)
    canvas.create_oval(305 ,20 , 505 , 220 , outline = 'black', width = 5)
    canvas.create_oval(525 ,20 , 725 , 220 , outline = '#ed334e', width = 5)
    canvas.create_oval(205 ,110 , 405 , 310 , outline = '#fbb132', width = 5)
    canvas.create_oval(425 ,110 , 625 , 310 , outline = '#1c8b3c', width = 5)



    window.mainloop()

olimpiadas()