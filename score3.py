import tkinter as tk
from tkinter import messagebox

def view_score():
    import score1
    exec("score1")

def scoreboard():
    import score2
    exec("score2")

def select():
    root.destroy()
    import damn
    exec("damn")



def image(smp):
    img = tk.PhotoImage(file="D:\\Shweta\\shweta 1(cd copy)\\villa\\hs-3\\images\\color\\10030.png")
    img = img.subsample(smp, smp)
    return img


def callback():
    if messagebox.askyesno('Verify', 'Are you leaving us so soon?!'):
        messagebox.showinfo('Yes', 'Goodbye!')
        root.destroy()
    else:
        messagebox.showinfo('No', 'Glad to have you back!')


root = tk.Toplevel()  # creates a simple GUI window

var1 = tk.IntVar()

root.title("Quitzie Score")
root['background'] = 'White'
but = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    activeforeground="light blue",
    activebackground="white",
    font="arial 30",
    text="",
    pady=10,
    padx=20
    # width=300
)

lbl1 = tk.Label(root, text="BILLIBOO!!Here's your SCORE!!", font=("Arial", 45), background="cyan", compound=tk.CENTER)
lbl1.grid()
img = image(2)  # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.grid()

B1 = tk.Button(root, text="View Score", font=("Arial", 18), command=view_score, background="White",
               compound=tk.CENTER).grid()
B2 = tk.Button(root, text="Scoreboard", font=("Arial", 18), command=scoreboard, background="White",
               compound=tk.CENTER).grid()
B3 = tk.Button(root, text="Quitzie Menu", font=("Arial", 18), command=select, background="White",
               compound=tk.CENTER).grid()
# B4=tk.Button(root,text="Quit",font=("Arial",18),command=callback,background="White",compound=tk.CENTER).grid()


root.mainloop()