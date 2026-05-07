from utils.logger import ProjektLogger
import tkinter as tk
from tkinter import messagebox

logger = ProjektLogger()
logger.infoprint("----------------------------")
logger.infoprint("START")

def nevjegy():
    messagebox.showinfo("Névjegy", "Objektum Orientált Programozás 'B' Beadandó Feladat\nRepülőjegy Foglalási Rendszer\nA programot készítette: Kupor Pál\nNeptun kód: G86X1Y")

root = tk.Tk()
root.title("Repülőjegy Foglalási Rendszer")
root.resizable(True, True)
root.minsize(800, 600)
root.state('zoomed')

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Kilépés", command=root.quit)

menu_bar.add_cascade(label="Fájl", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Névjegy", command=nevjegy)
menu_bar.add_cascade(label="Súgó", menu=help_menu)

label = tk.Label(root, text="Szia! Ez egy Python GUI.")
label.pack(pady=20)


button = tk.Button(root, text="Kattints ide", command=lambda: print("Gomb megnyomva!"))
button.pack()

root.config(menu=menu_bar)
root.mainloop()