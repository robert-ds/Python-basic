# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x300")
window.title("Lista de Compras")

elements_list = tk.Listbox(window,width=30)
elements_list.insert(0,"1Kg de Carne")
elements_list.insert(1,"12 huevos")
elements_list.insert(2,"2kg de Azucar")
elements_list.insert(3,"Detergente")
elements_list.insert(4,"2 litros de leche")
elements_list.insert(5,"Galletas")

elements_list.place(x=50,y=50)
etiq_lists = tk.Label(window,text="Lista").place(x=50,y=30)


window.mainloop()
