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
    window9['background'] = "white"
    lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window9, text="Q.10 Where does pineapple originate from?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window9, text="Mexico", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window9, text="Brazil", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window9, text="Hawaii", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window9, text="India", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window9, background="white")
    label.pack()



   

    B1 = Button(window9, text="Next", font=("Helvetica", 15), command=ab).pack()
    window9.mainloop()


# tells python to run the entire code and make a GUI


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
    
    window8.title("Questionairre")
    window8['background'] = "white"
    lbl = Label(window8, text="Question 9 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window8, text="Q.9 Common food sources of Vitamin A are", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window8, text="papayas, broccoli, tomatoes, kale", font=("Arial", 20), background="white").pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window8, text="Milk, eggs, butter, cheese, cream", font=("Arial", 20), background="white",
                     command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window8, text="Sugar, Sugar cane", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window8, text="tomatoes, brinjal, potatoes", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window8, background="white")
    label.pack()

    
    B1 = Button(window8, text="Next", font=("Helvetica", 15), command=windowI).pack()
    window8.mainloop()  # tells python to run the entire code and make a GUI


def windowG():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window6.destroy()
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

    global window7
    window7 = Tk()
    
    window7.title("Questionairre")
    window7['background'] = "white"
    lbl = Label(window7, text="Question 8 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window7, text="Q.8 Where does the Caesar salad originate from?", font=("Arial", 25),
                 background="cyan", compound=LEFT).pack()

    R1 = Radiobutton(window7, text="Canada", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window7, text="Mexico", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window7, text="Italy", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window7, text="India", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window7, background="white")
    label.pack()



    
    B1 = Button(window7, text="Next", font=("Helvetica", 15), command=windowH).pack()
    window7.mainloop()


# tells python to run the entire code and make a GUI


def windowF():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window5.destroy()
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

    global window6
    window6 = Tk()
    
    window6.title("Questionairre")
    window6['background'] = "white"
    lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window6, text="Q.7 Which country is famous for Mangoes?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window6, text="USA", font=("Arial", 20), background="white").pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window6, text="India", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window6, text="China", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window6, text="Korea", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window6, background="white")


    label.pack()



    



    B1 = Button(window6, text="Next", font=("Helvetica", 15), command=windowG).pack()
    window6.mainloop() # tells python to run the entire code and make a GUI


def windowE():
    import tkinter as tk
    window4.destroy()
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

    global window5
    window5 = Tk()
    
    window5.title("Questionairre")
    window5['background'] = "white"

    lbl = Label(window5, text="Question 6 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window5, text="Q.6 Common food sources of Vitamin D are", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window5, text="papayas", font=("Arial", 20), background="white").pack(
        anchor=NW)  
    R2 = Radiobutton(window5, text="eggs", font=("Arial", 20), background="white",
                     command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window5, text="Sugar cane", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window5, text="brinjal", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window5, background="white")
    label.pack()



    B1 = Button(window5, text="Next", font=("Helvetica", 15), command=windowF).pack()
    window5.mainloop()


def windowD():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window3.destroy()
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

    global window4
    window4 = Tk()
    
    window4.title("Questionairre")
    window4['background'] = "white"
    lbl = Label(window4, text="Question 5 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window4, text="Q.5 Which place is known for apples in India ?", font=("Arial", 25),
                 background="cyan", compound=LEFT).pack()

    R1 = Radiobutton(window4, text="Jammu and Kashmir", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window4, text="Himachal Pradesh", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window4, text="Uttar Pradesh", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window4, text=" Punjab", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window4, background="white")
    label.pack()

    
    B1 = Button(window4, text="Next", font=("Helvetica", 15), command=windowE).pack()
    window4.mainloop()


# tells python to run the entire code and make a GUI


def windowC():
    import tkinter as tk
    # imports the tkinter module of python which is a GUI
    window2.destroy()
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

    global window3
    window3 = Tk()
    
    window3.title("Questionairre")
    window3['background'] = "white"

    lbl = Label(window3, text="Question 4 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window3, text="Q.4 Which is the National food of India?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window3, text="Dal", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window3, text="Khichdi", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window3, text="Roti", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window3, text="Dosa", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window3, background="white")
    label.pack()



    B1 = Button(window3, text="Next", font=("Helvetica", 15), command=windowD).pack()
    window3.mainloop()


# tells python to run the entire code and make a GUI


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
    
    window2.title("Questionairre")
    window2['background'] = "white"
    lbl = Label(window2, text="Question 3 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window2, text="Q.3 Where are bananas originally from?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window2, text="Europe", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window2, text="South East Asia", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window2, text="Mexico", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window2, text="Italy", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window2, background="white")
    label.pack()



   
    B1 = Button(window2, text="Next", font=("Helvetica", 15), command=windowC).pack()
    window2.mainloop()  # tells python to run the entire code and make a GUI


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
    
    window1.title("Questionairre")
    window1['background'] = "white"

    lbl = Label(window1, text="Question 2 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window1, text="Q.2 Strawberry is good source of which vitamin?", font=("Arial", 25),
                 background="cyan", compound=LEFT).pack()

    R1 = Radiobutton(window1, text="Vitamin A", font=("Arial", 20), background="white",).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window1, text="Vitamin C", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window1, text="Vitamin K", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window1, text="Vitamin D", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window1, background="white")
    label.pack()



    B1 = Button(window1, text="Next", font=("Helvetica", 15), command=windowB).pack()
    window1.mainloop()


# tells python to run the entire code and make a GUI

def Questions():
    import tkinter as tk  # imports the tkinter module of python which is a GUI
    from tkinter import Label


    def selection(b):
        global score
        selected = "You have selected an option,proceed to next"
        label.config(text=selected)
        if (b):
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window11
    window11 = Tk()
    
    window11.title("Questionairre")
    window11['background'] = "white"

    lbl = Label(window11, text="Question 1 of 10", font=("Arial", 15), background="White").pack()

    label1 = Label(window11, background="white")
    label1.pack()
    label2 = Label(window11, background="white")

    lbl1 = Label(window11, text="Q.1 Where does coffee originate from?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window11, text="korea", font=("Arial", 20), background="white").pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window11, text="Ethiopia", font=("Arial", 20), background="white", command=partial(selection, 1)).pack(anchor=NW)
    R3 = Radiobutton(window11, text="China", font=("Arial", 20), background="white").pack(anchor=NW)
    R4 = Radiobutton(window11, text="Denmark", font=("Arial", 20), background="white").pack(anchor=NW)

    label = Label(window11, background="white")
    label.pack()



    B1 = Button(window11, text="Next", font=("Helvetica", 15), command=windowA).pack()
    window11.mainloop() # tells python to run the entire code and make a GUI


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