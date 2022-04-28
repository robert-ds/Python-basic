import tkinter # Importamos la libreria

window = tkinter.Tk() # instanciamos la librera

label_saludo = tkinter.Label(window, text="Welcome", bg="blue", fg="white") # Creamos la etiqueta para la ventana
label_saludo.pack(ipadx=50,ipady=50, fill='x',side="left")

label_adios = tkinter.Label(window, text="Chau", bg="green", fg="white")
label_adios.pack(ipadx=50,ipady=50, expand=True )

window.mainloop() # Creamos el loop para mantener la ventana abierta
