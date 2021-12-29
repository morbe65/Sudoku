import tkinter as tk
import random
from tkinter.constants import NW
from typing import Sized
import events
from PIL import ImageTk, Image

winCanvas=None
win=None


def pattern(r,c):
 return (events.base*(r%events.base)+r//events.base+c)%events.side

def shuffle(s):
 return random.sample(s,len(s))

rows=[]
for g in shuffle(events.rBase):
 for r in shuffle(events.rBase):
  rows.append(g*events.base+r)
columns=[]
for g in shuffle(events.rBase):
 for c in shuffle(events.rBase):
  columns.append(g*events.base+c)
nums=shuffle(range(1,events.base*events.base+1))
events.sudoku=[ [nums[pattern(r,c)] for c in columns] for r in rows ]


def generateWin(window):
 prepreWin= Image.open("youwin.jpg")
 preWin=prepreWin.resize((400,300),Image.ANTIALIAS)
 global winCanvas
 global win
 winCanvas= tk.Canvas(master=window)
 win=ImageTk.PhotoImage(preWin)


def hasElement(x,y,adding):
 compare=[x,y]
 t_f= False

 for i in adding:
  if i == compare:
   return True
  else:
   t_f=False
 
 return t_f


def populate(level):
 #How many squares to give based on difficulty
 given=0
 if level== events.levels[0]:
  given=35
 elif level== events.levels[1]:
  given=28
 elif level== events.levels[2]:
  given=80
 
 adding=[]
 counter=0
 #Randomly choosing what squares to give
 while counter < given:
  i=random.randint(0,8)
  j=random.randint(0,8)
  addingj=[]
  if not hasElement(i,j,adding):
   addingj.append(i)
   addingj.append(j)
   adding.append(addingj)
   counter+=1
 return adding

  
def generateBoard(window):
 adding= populate("Hard")
 playerColumn= []
 button = None
 for x in range(9):
  for y in range(9):  
   frame= tk.LabelFrame(master=window)
   frame.grid(row=x, column=y)
   if hasElement(x,y,adding)== True:
    button= tk.Button(master=frame, text=events.sudoku[x][y], font="Helvetica 12 bold")
    button.grid(row=x,column=y)
    playerColumn.append(events.sudoku[x][y])
   else:
    button=tk.Button(master=frame,command= lambda row = x, column = y, window=window: events.handle_click(row, column,window))
    button.grid(row=x,column=y)
    playerColumn.append("")
   
  events.playerboard.append(playerColumn) 
  playerColumn=[]
   

def correct():
 winner=True
 for row in range(9):
  for col in range(9):
   if events.sudoku[row][col]!= events.playerboard[row][col]:
    winner=False
 if winner: 
  print("You Win")
  winCanvas.create_image(0,0, anchor= NW, image= win)
  winCanvas.grid(row=0,column=0,columnspan=9,rowspan=9)
 else: print("Not Quite. Try Again!")

# class sudokuBoard(temp):
#     def __init__(self, temp):
#      self.temp = self.generateBoard(temp)
#     def generateBoard(self, temp):
#      board=[]
        
#      return board