from random import randint
import tkinter as tk

#Global Variables
currentwidget=None
currentwidgetbut=None
currentx=None
currenty=None
playerboard=[]
base=3
side= base*base
rBase=range(base)

levels= ["Easy","Medium","Hard","Test"]
sudoku=[]

def handle_keypress(event):
 x=event.char
 if str.isnumeric(x):
  if int(x) >=10 or int(x)<=0:
      print("Invalid Number")
  else:
     if currentwidget.cget("text") == x:
      currentwidgetbut.configure(text=x)
      currentwidget.configure(text="")
      global playerboard
      playerboard[currentx][currenty]=int(x)
      print(playerboard)
     else: 
      currentwidget.configure(text=x)
 else:
  print("Not a number")
  

def handle_click(row,col,window):
 widget= window.grid_slaves(row=row,column=col)[0]
 global currentwidget
 #widget.configure(text="yes")
 currentwidget=widget
 widgetbut=widget.winfo_children()[0]
 global currentwidgetbut
 currentwidgetbut=widgetbut
 global currentx
 currentx=row
 global currenty
 currenty=col
 print("x:{} y:{}".format(currentx,currenty))
 #widgetbut.configure(text="poo")


