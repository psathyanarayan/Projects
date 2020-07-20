import random
import tkinter
import IPython.display as display
from PIL import Image
def btnClick():
    x = random.choice([1,2,3,4,5,6])
    if x==1:
        img = Image.open("1.png")
        display.display(img.resize((50,50)))
    elif x==2:
        img = Image.open("2.png")
        display.display(img.resize((50,50)))
    elif x==3:
        img = Image.open("3.png")
        display.display(img.resize((50,50)))
    elif x==4:
        img = Image.open("4.png")
        display.display(img.resize((50,50)))
    elif x==5:
        img = Image.open("5.png")
        display.display(img.resize((50,50)))
    else:
       img = Image.open("6.png")
       display.display(img.resize((50,50)))    
            
tk = tkinter.Tk()
tk.geometry("400x400")
tk.title('Roll')
btn = tkinter.Button(tk, text = 'Click Here To Roll', width = '20',height='10',command = btnClick).place(x="100",y="100")
tk.mainloop()