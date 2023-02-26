#importing modules
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
import tkinter.font as font 
from functools import partial
from tkinter import messagebox
from tkinter import ttk


#creating the window
window=tk.Tk()
window.geometry('500x600')
window.title('Unit converter')
window.configure(bg='peach puff2')

#creating the fonts
font1=font.Font(family='helvetica',size='30')
font2=font.Font(family='helvetica',size='10')
font3=font.Font(family='helvetica',size='20')

#all functions
#selected function
def selected():
    pass

#fromfunc function
def fromfunc():
    pass

#creating tofunc function 
def tofunc():
    pass

#creating the unit converter
main=tk.Label(window,text='unit converter',bg='peach puff2',fg='blue')
main['font']=font1
main.place(relx='0.48',rely='0.1',anchor='center')

#creating unit label
unit=tk.Label(window,text='Unit -:',bg="peach puff2")
unit['font']=font2
unit.place(relx='0.25',rely='0.28')

#creating the main combobox
n=StringVar()
unitdd=ttk.Combobox(window,width='35',textvariable=n)

#values
unitdd['values']=('Volume',
                  'Length',
                  'Mass')
unitdd.place(relx='0.57',rely='0.3',anchor='center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

#creating the from label
label_from=tk.Label(window,text='From -:',bg='peach puff2')
label_from['font']=font2
label_from.place(relx='0.238',rely='0.37')

#creating the fromdd
f=StringVar()
fromdd=ttk.Combobox(window,width='35',textvariable=f)

fromdd.place(relx='0.57',rely='0.39',anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

#creating to label
to=tk.Label(window,text='To -:',bg='peach puff2')
to['font']=font2
to.place(relx='0.268',rely='0.45')

#creating  to drop down
t=StringVar()
todd=ttk.Combobox(window,width=35,textvariable=t)

todd.place(relx='0.57',rely='0.47',anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

#creating result label
result=tk.Label(window,text='',bg='white',width=20)
result['font']=font3
result.place(relx='0.21',rely='0.6')

#creating get_answer button
get_answer=tk.Button(window,text='Get Answer',bg='cyan2')
get_answer['font']=font2
get_answer.place(relx='0.46',rely='0.7')


#creating main loop
window.mainloop()
