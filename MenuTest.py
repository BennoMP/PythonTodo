from tkinter import *
from PIL import ImageTk, Image
import tkinter.ttk as ttk

def append():
    f= open("Todo.dat", "a+")
    print('Put the thing you wish to add here')
    addtofile = input()
    f.write(addtofile + "\r\n")

def clearfile():
    print('(Re)created todos')
    f= open("Todo.dat", "w")
    f.write("Todo list: \r\n")
    f.close()

def todo():
    f= open("Todo.dat", "r")
    if f.mode == 'r':
        contents =f.read()

#    List = Tk()
    List = Toplevel()
    List.geometry("385x500")
    List.title("List")
    canvas = Canvas(List)
    List.resizable(False, False)
    canvas.pack()

    image = Image.open("724-472x336.jpg")
    List.logo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=List.logo, anchor='nw')

    text = Text(List)
    S = Scrollbar(List)
    S.config(command=Text.yview)
    text.insert(INSERT, contents)
    text.config(state=DISABLED)
    text.pack()

    buttonA = Button(List, text='Exit to main', command=List.destroy)
    buttonA.pack()
    button_window = canvas.create_window(0, 0, anchor='nw', window=buttonA)

    buttonB = Button(List, text='(Re)create Todo list (removes all todos if it already exists)', command=clearfile)
    buttonB.pack()
    button_window = canvas.create_window(0, 40, anchor='nw', window=buttonB)

    List.mainloop()

def leave():
    quit()

def createnew():
    print('Created save file')
    f= open("Todo.dat","w+")
    f.write("Todo list: \r\n")
    f.close()
    

Main = Tk()
Main.geometry("230x160")
Main.title("Main Menu")
canvas = Canvas(Main)
Main.resizable(False, False)
canvas.pack()

image = Image.open("724-472x336.jpg")
Main.logo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=Main.logo, anchor='nw')

buttonA = Button(Main, text='Add something (in CLI)', command=append)
buttonA.pack()
button_window = canvas.create_window(10, 10, anchor='nw', window=buttonA)

buttonB = Button(Main, text='View list', command=todo)
buttonB.pack()
button_window = canvas.create_window(10, 50, anchor='nw', window=buttonB)

buttonC = Button(Main, text='Exit', command=leave)
buttonC.pack()
button_window = canvas.create_window(10, 90, anchor='nw', window=buttonC)

buttonD = Button(Main, text='I\'m new', command=clearfile)
buttonD.pack()
button_window = canvas.create_window(10, 130, anchor='nw', window=buttonD)

Main.mainloop()
