import tkinter
from tkinter import ttk
def mostrar():
    clear = tkinter.Label(window, text = "                      ")
    clear.grid(column = 1, row = 4,padx = 5,pady=5)
    nombre = ttk.Label(window, text = "{}".format(seleccion.get()))
    nombre.grid(column = 1, row = 4,padx = 5,pady=5)
def reboot(event):
    clear = ttk.Label(window, text = "                      ")
    clear.grid(column = 1, row = 4,padx = 5,pady=5)
    seleccion.set(None)

window = tkinter.Tk()
window.columnconfigure(1,weight = 3)
window.columnconfigure(2,weight=3)
window.columnconfigure(3,weight=3)

seleccion = tkinter.StringVar()
seleccion.set(None)
r1 = ttk.Radiobutton(window,text = 'Agua',value='Agua',variable = seleccion, command = mostrar)
r2 = ttk.Radiobutton(window,text = 'Pepsi',value='Pepsi',variable = seleccion, command = mostrar)
r3 = ttk.Radiobutton(window,text = 'Coca Cola',value='Coca Cola',variable = seleccion, command = mostrar)
clear = tkinter.Label(window, text = "                      ")
    
botonReboot =tkinter.Button(window, text = 'Reiniciar')
botonReboot.bind('<Button-1>',reboot)

r1.grid(column = 0,row =1,pady=3, padx =3)
r2.grid(column = 0,row =2,pady=3, padx =3)
r3.grid(column = 0,row =4,pady=3, padx =3)
clear.grid(column = 1, row = 4,padx = 5,pady=5)
botonReboot.grid(column = 3,row =4,pady=3, padx =3)

window.mainloop()
