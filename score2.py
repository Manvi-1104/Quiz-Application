import mysql.connector as sql

import tkinter as tk

window = tk.Tk()
window.title("View Scoreboard")
window['background'] = "White"
try:

    mydb = sql.connect(
        host="localhost",
        user="root",
        passwd="1234",
        charset="utf8", database="Quiz")
    mycursor = mydb.cursor()

    command = mycursor.execute("SELECT * FROM Scoreboard ORDER BY SCORE DESC")
    command1 = mycursor.fetchall()

    # lbl1=tk.Label(window, text="Scoreboard",font=("Arial",30),background="cyan",compound=tk.CENTER)
    # lbl1.grid()
    lab1 = tk.Label(window, text="Quiz Code", font=("Arial", 25), background="cyan", compound=tk.CENTER)
    lab1.grid(column=0, row=1)
    lbl2 = tk.Label(window, text="Name", font=("Arial", 25), background="cyan", compound=tk.CENTER).grid(column=1,
                                                                                                         row=1)
    lbl3 = tk.Label(window, text="Score", font=("Arial", 25), background="cyan", compound=tk.CENTER).grid(column=4,
                                                                                                          row=1)
    for i in range(len(command1)):
        label1 = tk.Label(window, text=command1[i][0], background="white", borderwidth=1, font=("Arial", 15),
                          relief="solid")
        label1.grid(column=1, row=i + 2)

        label2 = tk.Label(window, text=command1[i][1], background="white", borderwidth=1, font=("Arial", 15),
                          relief="solid")
        label2.grid(column=4, row=i + 2)

        label3 = tk.Label(window, text=command1[i][2], background="white", borderwidth=1, font=("Arial", 15),
                          relief="solid")
        label3.grid(column=0, row=i + 2)
    exit_button = tk.Button(window, text="Exit", font=("Arial", 13), command=window.destroy)
    exit_button.grid(column=1, row=len(command1) + 2)

except sql.InternalError as e:
    print("InternalError")
    print(e)

window.mainloop()