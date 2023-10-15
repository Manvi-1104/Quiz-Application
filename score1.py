import tkinter as tk
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="1234",
    auth_plugin='mysql_native_password',
    database="Quiz")
mycursor = mydb.cursor()

window = tk.Tk()


def Score():
    Name = Namefield.get()
    print(Name)
    command1 = mycursor.execute("SELECT * FROM Scoreboard")
    print(command1)
    command2 = mycursor.fetchall()
    print(command2)
    for i in range(len(command2)):
        if str(command2[i][0]) == Name:

            label1 = tk.Label(window, text=command2[i][0], background="white", font=("Arial", 15), borderwidth=1,
                              relief="solid")
            label1.grid(column=3, row=i + 3)

            label1 = tk.Label(window, text=command2[i][2], background="white", font=("Arial", 15), borderwidth=1,
                              relief="solid")
            label1.grid(column=0, row=i + 3)
            label11 = tk.Label(window, text=command2[i][1], background="white", font=("Arial", 15), borderwidth=1,
                               relief="solid")
            label11.grid(column=4, row=i + 3)
            if (variable1.get() == "Food Quiz"):

                label2 = tk.Label(window, text="Food Quiz", background="white", font=("Arial", 15), borderwidth=1,
                                  relief="solid")
                label2.grid(column=1, row=i + 3)
            elif (variable1.get() == "World Quiz"):
                label2 = tk.Label(window, text="World Quiz", background="white", font=("Arial", 15), borderwidth=1,
                                  relief="solid")
                label2.grid(column=1, row=i + 3)

            elif (variable1.get() == "Science Quiz"):
                label2 = tk.Label(window, text="Science Quiz", background="white", font=("Arial", 15), borderwidth=1,
                                  relief="solid")
                label2.grid(column=1, row=i + 3)

            else:
                label2 = tk.Label(window, text="Sports Quiz", background="white", font=("Arial", 15), borderwidth=1,
                                  relief="solid")
                label2.grid(column=1, row=i + 3)


window.title("Player Info")
window['background'] = "White"
var1 = tk.StringVar(window)
lbl1 = tk.Label(window, text="View Score:", font=("Arial", 30), background="cyan", compound=tk.CENTER)
lbl1.grid(column=0, row=0)
lbl3 = tk.Label(window, text="Player Name:", font=("Arial", 20), background="White", compound=tk.CENTER)
lbl3.grid(column=0, row=1)
lbl2 = tk.Label(window, text="Quiz Code", font=("Arial", 17), background="White", compound=tk.CENTER).grid(column=0,
                                                                                                           row=2)
lbl2 = tk.Label(window, text="Name", font=("Arial", 17), background="White", compound=tk.CENTER).grid(column=3, row=2)
lbl4 = tk.Label(window, text="Score", font=("Arial", 17), background="White", compound=tk.CENTER).grid(column=4, row=2)
lbl5 = tk.Label(window, text="Choice:", font=("Arial", 20), background="White", compound=tk.CENTER).grid(column=3,
                                                                                                         row=1)
lbl6 = tk.Label(window, text="Topic", font=("Arial", 17), background="White", compound=tk.CENTER).grid(column=1, row=2)
Namefield = tk.Entry(window)
Namefield.grid(column=1, row=1)
B1 = tk.Button(window, text="Enter", font=("Arial", 15), command=Score, compound=tk.CENTER)
B1.grid(column=1, row=100)
choice = ["Food Quiz", "World Quiz", "Science Quiz", "Sports Quiz"]
variable1 = tk.StringVar(window)
variable1.set(choice[0])

field1 = tk.OptionMenu(window, variable1, *choice)
field1.grid(column=4, row=1)

mydb.commit()
window.mainloop()

