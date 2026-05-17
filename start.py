from utils.logger import ProjektLogger
from utils.localize import Localize
import tkinter as tk
from tkinter import messagebox

logger = ProjektLogger()
logger.infoprint("----------------------------")
logger.infoprint("START")

language = 'hu'

def nevjegy():
    messagebox.showinfo(Localize.get_text('menu_about',language), Localize.get_text('aboutmessage',language))

root = tk.Tk()
root.title(Localize.get_text('windowtitle',language))
root.resizable(True, True)
root.minsize(800, 600)
root.state('zoomed')

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label=Localize.get_text('menu_exit',language), command=root.quit)

menu_bar.add_cascade(label=Localize.get_text('menu_file',language), menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label=Localize.get_text('menu_about',language), command=nevjegy)
menu_bar.add_cascade(label=Localize.get_text('menu_help',language), menu=help_menu)

label = tk.Label(root, text="Szia! Ez egy Python GUI.")
label.pack(pady=20)


button = tk.Button(root, text="Kattints ide", command=lambda: print("Gomb megnyomva!"))
button.pack()

root.config(menu=menu_bar)
root.mainloop()