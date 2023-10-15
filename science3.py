global score
global score1
score = 0
score1 = 0
a = 0
from functools import partial

def ab():
    if a == 0:
        import score3
        exec("score3")
        window9.destroy()



def windowI():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window8.destroy()

    def selection(b):
        global score
        global score1
        selected = "you have selected an option, proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print("Correct!Your final score is=", score)
            score1 = score
            print("YOUR TOTAL SCORE IS=", score1)
            val1 = (score1)
            string1 = "INSERT INTO SCOREBOARD(NAME,AGE,SCORE) VALUES(%s,%s,%s)"
            val = (Name, age, val1)
            print(Name)
            print(score)
            print(age)
            mycursor.execute(string1, val)
            mydb.commit()

        else:
            score += 0
            print("Wrong!Your final score is=", score)
            score1 = score
            print("YOUR TOTAL SCORE IS=", score1)

    global window9
    window9 = Tk()
    
    window9.title("questionairre")
    window9['background'] = "White"
    lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window9, text="Q.10 Which is the vertibrate that has two chambered heart ?",
                font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window9, text="Snake", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window9, text="Fish", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window9, text="Crocodile", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window9, text="Lizard", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window9)
    label.pack()
    B1 = Button(window9, text="Next",
                font=("helvetica", 15), command=ab).pack()  # creates a button to move to next window...not linked yet
    window9.mainloop()  # tells python to run the entire code and make a GUI


def windowH():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window7.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window8
    window8 = Tk()
    
    window8.title("questionairre")
    window8['background'] = "White"
    lbl = Label(window8, text="Question 9 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window8, text="Q.9 Who is known as the Father of Modren Magnetism ? ?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window8, text="Newton", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window8, text="Pierre Weiss", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window8, text="Thomas Alva Edison", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window8, text="Einsten", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window8)
    label.pack()
    B1 = Button(window8, text="Next", font=("helvetica", 15),
                command=windowI).pack()  # creates a button to move to next window...not linked yet
    window8.mainloop()  # tells python to run the entire code and make a GUI


def windowG():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window6.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window7
    window7 = Tk()
    
    window7.title("questionairre")
    window7['background'] = "White"
    lbl = Label(window7, text="Question 8 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window7, text="Q.8 What is the life span of the RBC?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window7, text="115 days", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window7, text="110 days", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window7, text="100 days", font=("Arial", 20), background="White",).pack(anchor=NW)
    R4 = Radiobutton(window7, text="120 days", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window7)
    label.pack()
    B1 = Button(window7, text="Next", font=("helvetica", 15),
                command=windowH).pack()  # creates a button to move to next window...not linked yet
    window7.mainloop()  # tells python to run the entire code and make a GUI


def windowF():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window5.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window6
    window6 = Tk()
    
    window6.title("questionairre")
    window6['background'] = "White"
    lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window6, text="Q.7 One pound is equal to?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window6, text="25.72g", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window6, text="100g", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window6, text="454g", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    R4 = Radiobutton(window6, text="200g", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window6)
    label.pack()
    B1 = Button(window6, text="Next", font=("helvetica", 15),
                command=windowG).pack()  # creates a button to move to next window...not linked yet
    window6.mainloop()  # tells python to run the entire code and make a GUI


def windowE():
    import tkinter as tk
    window4.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window5
    window5 = Tk()
    
    window5.title("questionairre")
    window5['background'] = "White"
    lbl = Label(window5, text="Question 6 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window5, text="Q.6 The number of ribs in human body is ?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window5, text="24", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window5, text="23", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window5, text="25", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window5, text="34", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window5)
    label.pack()
    B1 = Button(window5, text="Next", font=("helvetica", 15),
                command=windowF).pack()  # creates a button to move to next window...not linked yet
    window5.mainloop()


def windowD():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window3.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window4
    window4 = Tk()
    
    window4.title("questionairre")
    window4['background'] = "White"
    lbl = Label(window4, text="Question 5 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window4, text="Q.5 What is the smallest flightless bird ?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window4, text="Rhea", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window4, text="Kiwi", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window4, text="Penguin", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window4, text="Ostrich", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window4)
    label.pack()
    B1 = Button(window4, text="Next", font=("helvetica", 15),
                command=windowE).pack()  # creates a button to move to next window...not linked yet
    window4.mainloop()  # tells python to run the entire code and make a GUI


def windowC():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window2.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window3
    window3 = Tk()
    
    window3.title("questionairre")
    window3['background'] = "White"
    lbl = Label(window3, text="Question 4 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window3, text="Q.4 The process of preparing food in plants is called as ?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window3, text="Photosynthesis", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window3, text="Transpiration ", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window3, text="Translocation", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window3, text="Respiration", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window3)
    label.pack()
    B1 = Button(window3, text="Next", font=("helvetica", 15),
                command=windowD).pack()  # creates a button to move to next window...not linked yet
    window3.mainloop()  # tells python to run the entire code and make a GUI


def windowB():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window1.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window2
    window2 = Tk()
    
    window2.title("questionairre")
    window2['background'] = "White"
    lbl = Label(window2, text="Question 3 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window2, text="Q.3 Newton is the unit of ?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window2, text="Distance", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window2, text="Force", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window2, text="Displacement", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window2, text="Energy", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window2)
    label.pack()
    B1 = Button(window2, text="Next", font=("helvetica", 15),
                command=windowC).pack()  # creates a button to move to next window...not linked yet
    window2.mainloop()  # tells python to run the entire code and make a GUI


def windowA():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window11.destroy()
    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window1
    window1 = Tk()
    
    window1.title("questionairre")
    window1['background'] = "White"
    lbl = Label(window1, text="Question 2 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window1, text="Q.2 Depth of the ocean is measured by the instrument called ", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window1, text="Monometer", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window1, text="Fathometer", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window1, text="Lectometer", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window1, text="Photometer", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window1)
    label.pack()
    B1 = Button(window1, text="Next", font=("helvetica", 15),
                command=windowB).pack()  # creates a button to move to next window...not linked yet
    window1.mainloop()  # tells python to run the entire code and make a GUI


def Questions():
    import tkinter as tk  # imports the tkinter module of python which is a GUI
    from tkinter import Label


    def selection(b):
        global score
        selected="you have selected an option,proceed next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window11
    window11 = Tk()
    
    window11.title("questionairre")
    window11['background'] = "White"
    lbl = Label(window11, text="Question 1 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window11, text="Q.1 The fuel capacity of the Mars mission which was launched in India was?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window11, text="850kg", font=("Arial", 20), background="White", command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window11, text="405kg", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window11, text="800kg", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window11, text="600kg", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window11)
    label.pack()
    B1 = Button(window11, text="Next", font=("helvetica", 15), background="cyan",
                command=windowA).pack()  # creates a button to move to next window...not linked yet
    window11.mainloop()  # tells python to run the entire code and make a GUI


from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="1234",
    auth_plugin='mysql_native_password',
    database="Quiz")
mycursor = mydb.cursor()

window = Tk()


def check():
    global Name
    global age
    Name = Namefield.get()
    age = int(variable1.get())
    print(Name)
    print(score)
    print(age)
    Questions()


window.title("Player Info")
window['background'] = "White"
var1 = StringVar(window)
lbl1 = Label(window, text="Before We Begin:", font=("Arial", 30), background="cyan", compound=CENTER)
lbl1.pack(anchor=NW)
lbl3 = Label(window, text="Enter your Name:", font=("Arial", 20), background="White", compound=CENTER)
lbl3.pack(anchor=W)
Namefield = Entry(window)
Namefield.pack(anchor=NE)
lbl2 = Label(window, text="Enter your Age:", font=("Arial", 20), background="White", compound=CENTER)
lbl2.pack(anchor=W)
qty_list = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
variable1 = StringVar(window)
variable1.set(qty_list[12])
field1 = OptionMenu(window, variable1, *qty_list)
field1.pack(anchor=NE)
B1 = Button(window, text="Finish", font=("Arial", 15), command=check, compound=CENTER)
B1.pack(anchor=S)

mydb.commit()
window.mainloop()
