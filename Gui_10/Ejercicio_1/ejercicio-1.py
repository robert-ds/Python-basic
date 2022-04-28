# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.seleccion = tk.IntVar()
        self.seleccion.set(None)

        self.radio1 = tk.Radiobutton(self.ventana1,text="Male", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)

        self.radio2 = tk.Radiobutton(self.ventana1,text="Female", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)

        self.boton1 = tk.Button(self.ventana1, text="Show", command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)

        self.boton2 = tk.Button(self.ventana1, text="Reset", command=self.reset)
        self.boton2.grid(column=0, row=3)

        self.label1=tk.Label(self.ventana1,text=" ")
        self.label1.grid(column=0, row=4)

        self.ventana1.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get() == 1:
            self.label1.configure(text="Selected: Varon")
        if self.seleccion.get() == 2:
            self.label1.configure(text="Selected: Mujer")
    
    def reset(self):
    		if (self.seleccion.get() == 1 or self.seleccion.get() == 2):
    				self.seleccion.set(None)
    				self.label1.configure(text="")

app = Aplicacion() 


