#!/usr/bin/env python3
from easygui import *
import tkinter as tk

title = 'MiniCSC DataRun Logging script'


layers = ['L1','L2']
srcs = ['109-Cd','Sr-90']
holes = [1,2,3,4,5,6]

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

#label = tk.Label(
#    text='Hello World',
#    fg='white',
#    bg='black',
#    width='10',
#    height='10'
#)
#
#mbutton = tk.Button(
#    text='Layer 1',
#    width=25,
#    height=5,
#    bg='blue',
#    fg='yellow',
#)
#
#label.pack()
#mbutton.pack()

# Allows for listening
window.mainloop()
