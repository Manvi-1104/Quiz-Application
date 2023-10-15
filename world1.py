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
    radio = StringVar()
    window9.title("questionairre")
    window9['background'] = "White"
    lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window9, text="Q.10 Which is the largest ocean in world?",
                font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window9, text="Atlantic Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window9, text="Pacific Ocean", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window9, text="Indian Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window9, text="Arctic Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window9)
    label.pack()
    B1 = Button(window9, text="Next",
                font=("helvetica", 15), command=ab).pack()
    window9.mainloop()  


def windowH():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window7.destroy()
    def selection(b):
        global score
        selected = "you have selected an option,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window8
    window8 = Tk()
    radio = StringVar()
    window8.title("questionairre")
    window8['background'] = "White"
    lbl = Label(window8, text="Question 9 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window8, text="Q.9 Which country's ancient name is Mesopotamia?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window8, text="Bahrain", font=("Arial", 20), background="White",).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window8, text="Iraq", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window8, text="Iran", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window8, text="Israel", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window8)
    label.pack()
    B1 = Button(window8, text="Next", font=("helvetica", 15),
                command=windowI).pack()  
    window8.mainloop()  


def windowG():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window6.destroy()
    def selection(b):
        global score
        selected = "you have selected an option ,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window7
    window7 = Tk()
    radio = StringVar()
    window7.title("questionairre")
    window7['background'] = "White"
    lbl = Label(window7, text="Question 8 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window7, text="Q.8 Which city in India is know as 'Scotland of India'?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window7, text="Coorg", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window7, text="Darjelling", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window7, text="Mumbai", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window7, text="Assam", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window7)
    label.pack()
    B1 = Button(window7, text="Next", font=("helvetica", 15),
                command=windowH).pack()  
    window7.mainloop()  


def windowF():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window5.destroy()
    def selection(b):
        global score
        selected = "you have selected an option, proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window6
    window6 = Tk()
    radio = StringVar()
    window6.title("questionairre")
    window6['background'] = "White"
    lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window6, text="Q.7 How many countries border France?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window6, text="9", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window6, text="1", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window6, text="3", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    R4 = Radiobutton(window6, text="6", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window6)
    label.pack()
    B1 = Button(window6, text="Next", font=("helvetica", 15),
                command=windowG).pack()  
    window6.mainloop()  


def windowE():
    import tkinter as tk
    window4.destroy()
    def selection(b):
        global score
        selected = "you have selected an option ,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window5
    window5 = Tk()
    radio = StringVar()
    window5.title("questionairre")
    window5['background'] = "White"
    lbl = Label(window5, text="Question 6 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window5, text="Q.6 The Bermuda Triangle is located in which ocean?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window5, text="Atlantic Ocean", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window5, text="Pacific Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window5, text="Indian Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window5, text="Arctic Ocean", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window5)
    label.pack()
    B1 = Button(window5, text="Next", font=("helvetica", 15),
                command=windowF).pack()  
    window5.mainloop()


def windowD():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window3.destroy()
    def selection(b):
        global score
        selected = "you have selected an option ,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window4
    window4 = Tk()
    radio = StringVar()
    window4.title("questionairre")
    window4['background'] = "White"
    lbl = Label(window4, text="Question 5 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window4, text="Q.5 Which continent is also referred as a country?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window4, text="Australia", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window4, text="Africa", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window4, text="Europe", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window4, text="Russia", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window4)
    label.pack()
    B1 = Button(window4, text="Next", font=("helvetica", 15),
                command=windowE).pack()  
    window4.mainloop()  


def windowC():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window2.destroy()
    def selection(b):
        global score
        selected = "you have selected an option ,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window3
    window3 = Tk()
    radio = StringVar()
    window3.title("questionairre")
    window3['background'] = "White"
    lbl = Label(window3, text="Question 4 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window3, text="Q.4 Which river is the fastest flowing river in the world?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window3, text="Amazon", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window3, text="Congo", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window3, text="Brahamputra", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window3, text="Nile", font=("Arial", 20), background="White").pack(anchor=NW)
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
        selected = "you have selected an option,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window2
    window2 = Tk()
    radio = StringVar()
    window2.title("questionairre")
    window2['background'] = "White"
    lbl = Label(window2, text="Question 3 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window2, text="Q.3 Russia has how many time zones?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window2, text="1", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window2, text="11", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window2, text="3", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window2, text="10", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window2)
    label.pack()
    B1 = Button(window2, text="Next", font=("helvetica", 15),
                command=windowC).pack()  
    window2.mainloop()  


def windowA():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window11.destroy()
    def selection(b):
        global score
        selected = "you have selected an option,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)

    global window1
    window1 = Tk()
    radio = StringVar()
    window1.title("questionairre")
    window1['background'] = "White"
    lbl = Label(window1, text="Question 2 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window1, text="Q.2 Which country is known as land of midnight sun ?", font=("Arial", 25),
                background="cyan", compound=LEFT).pack()
    R1 = Radiobutton(window1, text="Hawaii", font=("Arial", 20), background="White").pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window1, text="Norway", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window1, text="Iceland", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window1, text="Detroit", font=("Arial", 20), background="White").pack(anchor=NW)
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
        selected = "you have selected an option,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window11
    window11 = Tk()
    radio = StringVar()
    window11.title("questionairre")
    window11['background'] = "White"
    lbl = Label(window11, text="Question 1 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window11, text="Q.1 Dead sea is located between which two countries?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window11, text="Jordan and Israel", font=("Arial", 20), background="White",command=partial(selection, 1)).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window11, text="Jordan and Sudan", font=("Arial", 20), background="White").pack(anchor=NW)
    R3 = Radiobutton(window11, text="Israel and UAE", font=("Arial", 20), background="White").pack(anchor=NW)
    R4 = Radiobutton(window11, text="UAE and Egypt", font=("Arial", 20), background="White").pack(anchor=NW)
    label = Label(window11)
    label.pack()
    B1 = Button(window11, text="Next", font=("helvetica", 15),
                command=windowA).pack()  # creates a button to move to next window...not linked yet
    window11.mainloop()


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
