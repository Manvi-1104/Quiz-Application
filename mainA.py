def world_quiz():
    import tkinter as tk

    def world_random():
        import random
        a = random.randint(1, 3)
        if a == 1:

            root.destroy()
            import world1
            exec("world1")

        elif a == 2:

            root.destroy()
            import world2
            exec("world2")

        else:

            root.destroy()
            import world3
            exec("world3")

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
        img = img.subsample(smp, smp)
        return img

    root = tk.Toplevel()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)

    var1 = tk.IntVar()

    root.title("World Geography Quitzie")
    root['background'] = 'White'
    but = tk.Button(
        root,
        bd=0,
        relief="raised",
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

    lbl1 = tk.Label(root, text="Welcome To The World QUIZZ!", font=("Arial", 53), background="cyan", compound=tk.CENTER)
    lbl1.pack()
    img = image(1)  # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()

    B1 = tk.Button(root, text="Start the Quiz", font=("Arial", 23), command=world_random, background="White", padx=10,
                   compound=tk.CENTER).pack()
    B1 = tk.Button(root, text="Quiz Menu", font=("Arial", 23), command=Quiz_Menu, background="White",
                   compound=tk.CENTER).pack()

    root.mainloop()


def food_quiz():
    import tkinter as tk

    def food_random():
        import random
        a = random.randint(1, 3)
        if a == 1:

            root.destroy()
            import food1
            exec("food1")

        elif a == 2:

            root.destroy()
            import food2
            exec("food2")

        else:

            root.destroy()
            import food3
            exec("food3")

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
        img = img.subsample(smp, smp)
        return img

    root = tk.Toplevel()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)

    var1 = tk.IntVar()

    root.title("Foodies Quitzie")
    root['background'] = 'White'
    but = tk.Button(
        root,
        bd=0,
        relief="raised",
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

    lbl1 = tk.Label(root, text="Welcome To The Foodie QUIZZ!", font=("Arial", 50), background="cyan",
                    compound=tk.CENTER)
    lbl1.pack()
    img = image(1)  # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()

    B1 = tk.Button(root, text="Start the Quiz", font=("Arial", 23), command=food_random, background="White", padx=10,
                   compound=tk.CENTER).pack()
    B1 = tk.Button(root, text="Quiz Menu", font=("Arial", 23), command=Quiz_Menu, background="White",
                   compound=tk.CENTER).pack()

    root.mainloop()


def science_quiz():
    import tkinter as tk

    def science_random():
        import random
        a = random.randint(1, 3)
        if a == 1:

            root.destroy()
            import science1
            exec("science1")

        elif a == 2:

            root.destroy()
            import science2
            exec("science2")

        else:

            root.destroy()
            import science3
            exec("science3")

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
        img = img.subsample(smp, smp)
        return img

    root = tk.Toplevel()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)

    var1 = tk.IntVar()

    root.title("Science Wizz Quitzie")
    root['background'] = 'White'
    but = tk.Button(
        root,
        bd=0,
        relief="raised",
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

    lbl1 = tk.Label(root, text="Welcome To The Science Wizz QUIZZ!", font=("Arial", 45), background="cyan",
                    compound=tk.CENTER)
    lbl1.pack()
    img = image(1)  # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()

    B1 = tk.Button(root, text="Start the Quiz", font=("Arial", 23), command=science_random, background="White", padx=10,
                   compound=tk.CENTER).pack()
    B1 = tk.Button(root, text="Quiz Menu", font=("Arial", 23), command=Quiz_Menu, background="White",
                   compound=tk.CENTER).pack()

    root.mainloop()


def sports_quiz():
    import tkinter as tk

    def sports_random():
        import random
        a = random.randint(1, 3)
        if a == 1:

            root2.destroy()
            import sports1
            exec("sports1")

        elif a == 2:

            root2.destroy()
            import sports2
            exec("sports2")

        else:

            root2.destroy()
            import sports3
            exec("sports3")

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
        img = img.subsample(smp, smp)
        return img

    root2 = tk.Toplevel()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root2.destroy)
    root2.config(menu=menu)

    var1 = tk.IntVar()

    root2.title("Sports Quitzie")
    root2['background'] = 'White'
    but = tk.Button(
        root2,
        bd=0,
        relief="raised",
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

    lbl1 = tk.Label(root2, text="Welcome To The Sports QUIZZ!", font=("Arial", 50), background="cyan",
                    compound=tk.CENTER)
    lbl1.pack()
    img = image(1)  # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()

    B1 = tk.Button(root2, text="Start the Quiz", font=("Arial", 23), command=sports_random, background="White", padx=10,
                   compound=tk.CENTER).pack()
    B1 = tk.Button(root2, text="Quiz Menu", font=("Arial", 23), command=Quiz_Menu, background="White",
                   compound=tk.CENTER).pack()

    root.mainloop()


def Quiz_Menu():
    root.destroy()
    import tkinter as tk

    def select():
        sel = var1.get()
        lbl1.configure(text=sel)

    def image(smp):
        img = PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
        img = img.subsample(smp, smp)
        return img

    root1 = Tk()

    menu = Menu()
    menu.add_command(label="Quit", command=root1.destroy)
    root1.config(menu=menu)

    var1 = IntVar()

    root1.title("Quitzie Menu")
    root1['background'] = 'White'
    but = Button(
        root1,
        bd=0,
        relief="groove",
        compound=CENTER,
        bg="white",
        activeforeground="light blue",
        activebackground="white",
        font="arial 30",
        text="",
        pady=10,
        padx=20
        # width=300
    )

    lbl1 = Label(root1, text="Choose your Quiz Topic!", font=("Arial", 53), background="cyan", compound=CENTER)
    lbl1.pack()
    img = image(1)  # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()

    B1 = Button(root1, text="World Quiz", font=("Arial", 23), command=world_quiz, background="White", padx=10).pack(
        side=LEFT)
    B2 = Button(root1, text="Sports Quiz", font=("Arial", 23), command=sports_quiz, background="White").pack(side=RIGHT)
    B3 = Button(root1, text="Food Quiz", font=("Arial", 23), command=food_quiz, background="White", padx=16).pack(
        side=LEFT)
    B4 = Button(root1, text="Science Quiz", font=("Arial", 23), command=science_quiz, background="White",
                compound=CENTER).pack()

    root1.mainloop()


from tkinter import *


def select():
    sel = var1.get()
    lbl1.configure(text=sel)  # used to access object's attributes after initialization


def image(smp):
    img = PhotoImage(file="C:\\Users\\santhos\\Desktop\\1.png")
    img = img.subsample(
        smp)  # Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
    return img


root = Tk()

menu = Menu()
menu.add_command(label="Quit", command=root.destroy)
root.config(menu=menu)

var1 = IntVar()  # holds integer data

root.title("Damnic Quitzie")
root['background'] = 'White'
but = Button(
    root,
    bd=0,
    relief="groove",
    compound=CENTER,
    bg="white",
    activeforeground="light blue",
    activebackground="white",
    pady=10,
    padx=20
    # width=300
)

lbl1 = Label(root, text="Welcome To The Quiz!", font=("Arial", 55), background="cyan", compound=CENTER)
lbl1.pack()
img = image(1)  # 1=normal, 2=small, 3=smallest
but.config(image=img)  # change the property of the widget
but.pack()  # make widget fill the entire frame and declares its position
lbl2 = Label(root, text="Press enter to begin", font=("Arial", 20), background="cyan").pack()

B1 = Button(root, text="Enter", font=("Arial", 25), relief="groove", background="White", command=Quiz_Menu,
            compound=CENTER).pack()

root.mainloop()