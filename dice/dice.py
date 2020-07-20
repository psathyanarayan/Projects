import random
import tkinter
from tkinter import Label
import IPython.display as display
from PIL import Image ,ImageTk
def btnClick():
    x = random.choice([1,2,3,4,5,6])
    if x==1:
        img = Image.open("1.png")
        img = img.resize((120,120))
        pic = ImageTk.PhotoImage(img)
        ig = Label(image = pic)
        ig.image = pic
        ig.place(x=120,y=120)
        display.display(img.resize((50,50)))
    elif x==2:
        img = Image.open("2.png")
        img = img.resize((120,120))
        pic = ImageTk.PhotoImage(img)
        ig = Label(image = pic)
        ig.image = pic
        ig.place(x=120,y=120)
        display.display(img.resize((50,50)))
    elif x==3:
        img = Image.open("3.png")
        img = img.resize((120,120))
        pic = ImageTk.PhotoImage(img)
        ig = Label(image = pic)
        ig.image = pic
        ig.place(x=120,y=120)
        display.display(img.resize((50,50)))
    elif x==4:
        img = Image.open("4.png")
        img = img.resize((120,120))
        pic = ImageTk.PhotoImage(img)
        ig = Label(image = pic)
        ig.image = pic
        ig.place(x=120,y=120)
        display.display(img.resize((50,50)))
    elif x==5:
        img = Image.open("5.png")
        img = img.resize((120,120))
        pic = ImageTk.PhotoImage(img)
        ig = Label(image = pic)
        ig.image = pic
        ig.place(x=120,y=120)
        display.display(img.resize((50,50)))
    else:
       img = Image.open("6.png")
       img = img.resize((120,120))
       pic = ImageTk.PhotoImage(img)
       ig = Label(image = pic)
       ig.image = pic
       ig.place(x=120,y=120)
       display.display(img.resize((50,50)))    
            
tk = tkinter.Tk()
tk.geometry("400x400")
tk.title('Roll')
btn = tkinter.Button(tk, text = 'Roll', width = '8',height='2',command = btnClick).place(x="150",y="300")
tk.mainloop()
