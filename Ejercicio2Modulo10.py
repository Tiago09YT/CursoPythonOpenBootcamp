import tkinter
from tkinter import ttk

window = tkinter.Tk()
lista = ['Windows','macOS', 'Linux', 'MS DOS']
frame = ttk.Frame(window)
frame1 = ttk.Frame(window)
listaItems = tkinter.StringVar(value = lista)
listBox = tkinter.Listbox(frame,height =6,listvariable =listaItems)
listBox.pack(fill = 'both', side = 'left')
texto = "A cuanto la carnita asada"
label = ttk.Label(frame1, text = texto)
label.pack(fill = 'both')
frame.pack(fill = 'both')
frame1.pack(ipadx = len(texto),fill = 'both')
window.mainloop()