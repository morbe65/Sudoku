#Imports
import tkinter as tk
import creation
import events
from PIL import ImageTk, Image


#Creates window
window= tk.Tk()
window.title("Sudoku")
background= tk.Canvas(master=window,background="black")
background.grid(row=0,column=0,columnspan=9,rowspan=9)

submit=tk.Button(master=window,text="Submit",command=creation.correct)
submit.grid(row=9,column=0,columnspan=9)

x=0
if x==0:
 creation.generateBoard(window)
 x+=1
 

window.bind("<Key>", events.handle_keypress)
creation.generateWin(window)

print(events.playerboard)
#Displays window
window.mainloop()
