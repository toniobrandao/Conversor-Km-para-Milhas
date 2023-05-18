# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:24:35 2023

@author: antoniobrandao
"""

import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("Conversor Km para Milhas")

window.minsize(width=500,height=300)

#window.config(padx=100,pady=200)

#Label


km_label = tkinter.Label(text="Km", font = ("Arial",24,"normal"))
km_label.grid(column=2,row=0)
equal_label =  tkinter.Label(text="é igual a ", font = ("Arial",24,"normal"))
equal_label.grid(column=0,row=1)

num_milhas_label =  tkinter.Label(text="0", font = ("Arial",24,"normal"))
num_milhas_label.grid(column=1,row=1)

milhas_label = tkinter.Label(text="milhas", font = ("Arial",24,"normal"))
milhas_label.grid(column=2,row=1)

def button_clicked():
    num_milhas_label["text"]=round(float(input.get())*0.62137273665,4)
    
    
    

button = Button(text="Calcular",command = button_clicked)
button.grid(column=1,row=2)


input = Entry(width = 10)
input.grid(column=1, row =0)
#loop to keep the window on screen.
window.mainloop()