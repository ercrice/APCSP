import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Hello World")

button = ttk.Button(window, text="My simple app.")
button.pack()


window.mainloop()
