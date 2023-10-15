
def science_quiz_q():
    
    def windowI():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window8.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window9
        window9 = Tk()
        radio = StringVar()
        window9.title("questionairre")
        window9['background'] = "White"
        lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()
        lbl = Label(window9, text="Q.10 The fuel capacity of the mars mission which was launched in india was ? ?",
                    font=("Arial", 25), background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window9, text="405kg", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window9, text="850kg", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window9, text="800kg", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window9, text="600kg", font=("Arial", 20), background="White", variable=radio, value=" wrong answer",
                         command=selection).pack(anchor=NW)
        label = Label(window9)
        label.pack()
        B1 = Button(window9, text="Next",
                    font=("helvetica", 15)).pack()  # creates a button to move to next window...not linked yet
        window9.mainloop()  # tells python to run the entire code and make a GUI


    def windowH():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window7.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window8, text="Q.9 Who is known as the Father of Modren Magnetism ? ?", font=("Arial", 25),
                    background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window8, text="Newton", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option ", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window8, text="Pierre Weiss", font=("Arial", 20), background="White", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window8, text="Thomas Alva Edison", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window8, text="Einsten", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window8)
        label.pack()
        B1 = Button(window8, text="Next", font=("helvetica", 15),
                    command=windowI).pack()  # creates a button to move to next window...not linked yet
        window8.mainloop()  # tells python to run the entire code and make a GUI


    def windowG():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window6.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window7, text="Q.8 Depth of the ocean is measured by an instrument called ?", font=("Arial", 25),
                    background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window7, text="Fathometer", font=("Arial", 20), background="White", variable=radio,
                         value="Correct choice", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window7, text="Lectometer", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window7, text="Photometer", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window7, text="Monometer", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window7)
        label.pack()
        B1 = Button(window7, text="Next", font=("helvetica", 15),
                    command=windowH).pack()  # creates a button to move to next window...not linked yet
        window7.mainloop()  # tells python to run the entire code and make a GUI


    def windowF():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window5.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window6, text="Q.7 One pound is equal to?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window6, text="25.72g", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window6, text="100g", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window6, text="454g", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window6, text="200g", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                         command=selection).pack(anchor=NW)
        label = Label(window6)
        label.pack()
        B1 = Button(window6, text="Next", font=("helvetica", 15),
                    command=windowG).pack()  # creates a button to move to next window...not linked yet
        window6.mainloop()  # tells python to run the entire code and make a GUI


    def windowE():
        import tkinter as tk
        window4.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window5, text="Q.6 Newton is the unit of?", font=("Arial", 25), background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window5, text="Force", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window5, text="Energy", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window5, text="Distance", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window5, text="Displacement", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window5)
        label.pack()
        B1 = Button(window5, text="Next", font=("helvetica", 15),
                    command=windowF).pack()  # creates a button to move to next window...not linked yet
        window5.mainloop()


    def windowD():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window3.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window4, text="Q.5 Which is the vertibrate the has two chambered heart?", font=("Arial", 25),
                    background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window4, text="Fish", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window4, text="Snake", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window4, text="Blue Whale", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window4, text="Crocodile", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option ", command=selection).pack(anchor=NW)
        label = Label(window4)
        label.pack()
        B1 = Button(window4, text="Next", font=("helvetica", 15),
                    command=windowE).pack()  # creates a button to move to next window...not linked yet
        window4.mainloop()  # tells python to run the entire code and make a GUI


    def windowC():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window2.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window3, text="Q.4 Which is the smallest flightless bird?", font=("Arial", 25), background="cyan",
                    compound=LEFT).pack()
        R1 = Radiobutton(window3, text="Rhea", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window3, text="Kiwi", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window3, text="Penguin", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window3, text="Ostrich", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        label = Label(window3)
        label.pack()
        B1 = Button(window3, text="Next", font=("helvetica", 15),
                    command=windowD).pack()  # creates a button to move to next window...not linked yet
        window3.mainloop()  # tells python to run the entire code and make a GUI


    def windowB():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window1.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window2, text="Q.3 The number of ribs in human body is?", font=("Arial", 25), background="cyan",
                    compound=LEFT).pack()
        R1 = Radiobutton(window2, text="23", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window2, text="24", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window2, text="25", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window2, text="22", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        label = Label(window2)
        label.pack()
        B1 = Button(window2, text="Next", font=("helvetica", 15),
                    command=windowC).pack()  # creates a button to move to next window...not linked yet
        window2.mainloop()  # tells python to run the entire code and make a GUI


    def windowA():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        
        window.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        lbl = Label(window1, text="Q.1 The process of preparing food in plants is called as", font=("Arial", 25),
                    background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window1, text="transpiration", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect option", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window1, text="photosynthesis", font=("Arial", 20), background="White", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window1, text="respiration", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window1, text="physiology", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window1)
        label.pack()
        B1 = Button(window1, text="Next", font=("helvetica", 15),
                    command=windowB).pack()  # creates a button to move to next window...not linked yet
        window1.mainloop()  # tells python to run the entire code and make a GUI


    import tkinter


    def selection():
        score = 0
        selected = "you have selected " + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    window = Tk()
    radio = StringVar()
    window.title("questionairre")
    window['background'] = "White"
    lbl = Label(window, text="Question 1 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window, text="Q.1 What is the life span of RBC?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window, text="115 days", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                     command=selection).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window, text="110 days", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                     command=selection).pack(anchor=NW)
    R3 = Radiobutton(window, text="100 days", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                     command=selection).pack(anchor=NW)
    R4 = Radiobutton(window, text="120 days", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                     command=selection).pack(anchor=NW)
    label = Label(window)
    label.pack()
    B1 = Button(window, text="Next", font=("helvetica", 15), background="cyan",
                command=windowA).pack()  # creates a button to move to next window...not linked yet
    window.mainloop()
def food_quiz_q():
    def windowI():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window8.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window9
        window9 = Tk()
        radio = StringVar()
        window9.title("questionairre")
        window9['background'] = "white"

        lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window9, text="Q.10  Which state is known as Apple state of India?", font=("Arial", 25),
                     background="cyan", compound=LEFT).pack()

        R1 = Radiobutton(window9, text="Jammu and Kashmir", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window9, text="Himachal Pradesh", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window9, text="Uttar Pradesh", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window9, text=" Punjab", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window9, background="white")
        label.pack()

        B1 = Button(window9, text="Next", font=("Helvetica", 15)).pack()
        window9.mainloop()


    # tells python to run the entire code and make a GUI


    def windowH():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window7.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window8
        window8 = Tk()
        radio = StringVar()
        window8.title("Questionairre")
        window8['background'] = "white"

        lbl = Label(window8, text="Question 9 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window8, text="Q.9 Which country is famous for Mangoes?", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window8, text="USA", font=("Arial", 20), background="white", variable=radio, value="wrong choice",
                         command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window8, text="India", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window8, text="China", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window8, text="Korea", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window8, background="white")


        label.pack()


        B1 = Button(window8, text="Next", font=("Helvetica", 15), command=windowI).pack()
        window8.mainloop()  # tells python to run the entire code and make a GUI


    def windowG():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window6.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window7
        window7 = Tk()
        radio = StringVar()
        window7.title("Questionairre")
        window7['background'] = "white"

        lbl = Label(window7, text="Question 8 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window7, text="Q.8 Where are bananas originally from?", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window7, text="Europe", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window7, text="South East Asia", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window7, text="Mexico", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window7, text="Italy", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window7, background="white")
        label.pack()


        B1 = Button(window7, text="Next", font=("Helvetica", 15), command=windowH).pack()
        window7.mainloop()


    # tells python to run the entire code and make a GUI


    def windowF():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window5.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window6
        window6 = Tk()
        radio = StringVar()
        window6.title("Questionairre")
        window6['background'] = "white"

        lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window6, text="Q.7 Common food sources of Vitamin A are", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window6, text="papayas, broccoli, tomatoes, kale", font=("Arial", 20), background="white",
                         variable=radio, value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window6, text="Milk, eggs, butter, cheese, cream", font=("Arial", 20), background="white",
                         variable=radio, value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window6, text="Sugar, Sugar cane", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window6, text="tomatoes, brinjal, potatoes", font=("Arial", 20), background="white",
                         variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window6, background="white")
        label.pack()



        B1 = Button(window6, text="Next", font=("Helvetica", 15), command=windowG).pack()
        window6.mainloop() # tells python to run the entire code and make a GUI


    def windowE():
        import tkinter as tk
        window4.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window5
        window5 = Tk()
        radio = StringVar()
        window5.title("Questionairre")
        window5['background'] = "white"

        lbl = Label(window5, text="Question 6 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window5, text="Q.6 Common food sources of Vitamin D are", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window5, text="papayas", font=("Arial", 20), background="white",
                         variable=radio, value="wrong choice", command=selection).pack(
            anchor=NW)  
        R2 = Radiobutton(window5, text="eggs", font=("Arial", 20), background="white",
                         variable=radio, value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window5, text="Sugar cane", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window5, text="brinjal", font=("Arial", 20), background="white",
                         variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window5, background="white")
        label.pack()



        B1 = Button(window5, text="Next", font=("Helvetica", 15), command=windowF).pack()
        window5.mainloop()


    def windowD():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window3.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window4
        window4 = Tk()
        radio = StringVar()
        window4.title("Questionairre")
        window4['background'] = "white"

        lbl = Label(window4, text="Question 5 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window4, text="Q.5 Where does pineapple originate from??", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window4, text="Mexico", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window4, text="Brazil", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window4, text="Hawaii", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window4, text="India", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window4, background="white")
        label.pack()


        B1 = Button(window4, text="Next", font=("Helvetica", 15), command=windowE).pack()
        window4.mainloop()


    # tells python to run the entire code and make a GUI


    def windowC():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window2.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window3
        window3 = Tk()
        radio = StringVar()
        window3.title("Questionairre")
        window3['background'] = "white"

        lbl = Label(window3, text="Question 4 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window3, text="Q.4 Where does coffee originate from?", font=("Arial", 25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window3, text="Canada", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window3, text="Ethiopia", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window3, text="Turkey", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window3, text="Denmark", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window3, background="white")
        label.pack()



        B1 = Button(window3, text="Next", font=("Helvetica", 15), command=windowD).pack()
        window3.mainloop()


    # tells python to run the entire code and make a GUI


    def windowB():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window1.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window2
        window2 = Tk()
        radio = StringVar()
        window2.title("Questionairre")
        window2['background'] = "white"

        lbl = Label(window2, text="Question 3 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window2, text="Q.3 Where does the Caesar salad originate from?", font=("Arial", 25),
                     background="cyan", compound=LEFT).pack()

        R1 = Radiobutton(window2, text="Canada", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window2, text="Mexico", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window2, text="Italy", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window2, text="India", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window2, background="white")
        label.pack()


        B1 = Button(window2, text="Next", font=("Helvetica", 15), command=windowC).pack()
        window2.mainloop()  # tells python to run the entire code and make a GUI


    def windowA():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window1
        window1 = Tk()
        radio = StringVar()
        window1.title("Questionairre")
        window1['background'] = "white"

        lbl = Label(window1, text="Question 2 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window1, text="Q.2 Strawberry is good source of which vitamin?", font=("Arial", 25),
                     background="cyan", compound=LEFT).pack()

        R1 = Radiobutton(window1, text="Vitamin A", font=("Arial", 20), background="white", variable=radio,
                         value="wrong choice", command=selection).pack(
            anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
        R2 = Radiobutton(window1, text="Vitamin C", font=("Arial", 20), background="white", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window1, text="Vitamin K", font=("Arial", 20), background="white", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window1, text="Vitamin D", font=("Arial", 20), background="white", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window1, background="white")
        label.pack()



        B1 = Button(window1, text="Next", font=("Helvetica", 15), command=windowB).pack()
        window1.mainloop()


    # tells python to run the entire code and make a GUI


    import tkinter  # imports the tkinter module of python which is a GUI
    from tkinter import Label


    def selection():
        score = 0
        selected = "You have selected " + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    window = Tk()
    radio = StringVar()
    window.title("Questionairre")
    window['background'] = "white"

    lbl = Label(window, text="Question 1 of 10", font=("Arial", 15), background="White").pack()

    label1 = Label(window, background="white")
    label1.pack()
    label2 = Label(window, background="white")

    lbl1 = Label(window, text="Q.1 Which is the national food of India?", font=("Arial", 25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window, text="Roti", font=("Arial", 20), background="white", variable=radio, value="wrong choice",
                     command=selection).pack(
        anchor=NW)  # creates radiobuttons as to be chosen by the user....only one at a time
    R2 = Radiobutton(window, text="Khichdi", font=("Arial", 20), background="white", variable=radio,
                     value="correct choice", command=selection).pack(anchor=NW)
    R3 = Radiobutton(window, text="Dal", font=("Arial", 20), background="white", variable=radio, value="wrong option",
                     command=selection).pack(anchor=NW)
    R4 = Radiobutton(window, text="Curry", font=("Arial", 20), background="white", variable=radio,
                     value="incorrect choice", command=selection).pack(anchor=NW)

    label = Label(window, background="white")
    label.pack()



    B1 = Button(window, text="Next", font=("Helvetica", 15), command=windowA).pack()
    window.mainloop() 
def sports_quiz_q():
    
    def windowI():
        import tkinter as tk
        window8.destroy()
        def selection():
            score=0
            selected="you have selected "+str(radio.get())
            label.config(text=selected)
            if str(radio.get())=="correct choice":
                score+=10
                print(score)
            else:
                score+=0
                print(score)

        global window9
        window9=Tk()
        radio=StringVar()
        window9.title("questionairre")
        window9["background"]="white"
        lbl = Label(window9, text="Question 10 of 10", font=("Arial",15),background="white").pack()

        lbl1 = Label(window9, text="Q.10 Which player has the highest rating in chess", font=("Arial",25),background="cyan", compound=LEFT).pack()

        R1=Radiobutton(window9, text="Vishwanathananand", font=("Arial",20),background="White",
                             variable=radio, value="Wrong choice", command=selection).pack(anchor=NW)
        R2 =Radiobutton(window9, text="Garry kasparov", font=("Arial", 20),background="White",
                             variable=radio, value="wrong option", command=selection).pack(anchor=NW)
        R3 =Radiobutton(window9, text="vladimir kramnink", font=("Arial", 20),background="White",
                             variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)
        R4 =Radiobutton(window9, text="Magnus Carlsen", font=("Arial", 20),background="White",
                             variable=radio, value="correct choice", command=selection).pack(anchor=NW)

        label = Label(window9)
        label.pack()

        B1 = Button(window9, text="Next", font=("Helvetica",15)).pack()
        window9.mainloop()


    def windowH():
        import tkinter as tk
        window7.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window8
        window8 = Tk()
        radio = StringVar()
        window8.title("questionairre")
        window8["background"] = "white"

        lbl = Label(window8, text="Question 9 of 10", font=("Arial",15),background="white").pack
        lbl1=Label(window8,text="Q9.Which sport does not use the term ring?",font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1 = Radiobutton(window8, text="Boxing", font=("Arial",20),background="white",
                         variable=radio, value="Wrong choice", command=selection).pack(anchor=NW)
        R2 = Radiobutton(window8, text="Gymnastics", font=("Arial",20),background="white",
                         variable=radio, value="wrong option", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window8, text="Icehockey", font=("Arial",20),background="white",
                         variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window8, text="Baseball", font=("Arial",20),background="white",
                         variable=radio, value="correct choice", command=selection).pack(anchor=NW)

        label = Label(window8)
        label.pack()

        B1 = Button(window8, text="Next", font=("Helvetica",15),command=windowI).pack()
        window8.mainloop()



    def windowG():
        import tkinter as tk
        window6.destroy()
        def selection():
            score=0
            selected="you have selected "+str(radio.get())
            label.config(text=selected)
            if str(radio.get())=="correct choice":
                score+=10
                print(score)
            else:
                score+=0
                print(score)
        global window7
        window7=Tk()
        radio=StringVar()
        window7.title("questionairre")
        window7["background"]="white"
        lbl=Label(window7,text="Question 8 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window7,text="Q.8 When was the SportAccord renamed as the GASIF?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1=Radiobutton(window7,text=2005,font=("Arial",20),background="White",
        variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window7,text=2017,font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R3=Radiobutton(window7,text=2016,font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)
        R4=Radiobutton(window7,text=2010,font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)

        label=Label(window7)
        label.pack()

        B1=Button(window7,text="Next",font=("Helvetica",15),command=windowH).pack()
        window7.mainloop()


    def windowF():
        import tkinter as tk
        window5.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window6
        window6 = Tk()
        radio = StringVar()
        window6.title("questionairre")
        window6["background"] = "white"
        lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()

        lbl1 = Label(window6, text="Q.7 Which cricket team won the 2019-2020 Vijay Hazare Trophy?", font=("Arial",25), background="cyan",
                     compound=LEFT).pack()

        R1 = Radiobutton(window6, text="Karnataka", font=("Arial", 20), background="White",
                         variable=radio, value="correct choice", command=selection).pack(anchor=NW)
        R2 = Radiobutton(window6, text="Himachal Pradesh", font=("Arial",20), background="White",
                         variable=radio, value="wrong choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window6, text="Maharahstra", font=("Arial",20), background="White",
                         variable=radio, value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window6, text="Delhi", font=("Arial",20), background="White",
                         variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)

        label = Label(window6)
        label.pack()

        B1 = Button(window6, text="Next", font=("Helvetica",15),command=windowG).pack()
        window6.mainloop()

    def windowE():
        import tkinter as tk
        window4.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window5
        window5 = Tk()
        radio = StringVar()
        window5.title("questionairre")
        window5["background"] = "white"


        lbl=Label(window5,text="Question 6 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window5,text="Q.6 Which cricket team won the semifinals but lost in the finals of the world cup 2019?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1=Radiobutton(window5,text="India",font=("Arial",20),background="White",
        variable=radio,value="Wrong choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window5,text="Australia",font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)
        R3=Radiobutton(window5,text="Newzealand",font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R4=Radiobutton(window5,text="England",font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

        label=Label(window5)
        label.pack()

        B1=Button(window5,text="Next",font=("Helvetica",15),command=windowF).pack()
        window5.mainloop()

    def windowD():
        import tkinter as tk
        window3.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window4
        window4 = Tk()
        radio = StringVar()
        window4.title("questionairre")
        window4["background"] = "white"

        lbl=Label(window4,text="Question 5 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window4,text="Q.5 Which player is given the title of the flying sikh?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1=Radiobutton(window4,text="Milkha Singh",font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window4,text="Bahadur Singh Chauhan",font=("Arial",20),background="White",
        variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
        R3=Radiobutton(window4,text="Kamaljeet Sandhu",font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)
        R4=Radiobutton(window4,text="Harmanpreet singh",font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

        label=Label(window4)
        label.pack()

        B1=Button(window4,text="Next",font=("Helvetica",15),command=windowE).pack()
        window4.mainloop()

    def windowC():
        import tkinter as tk
        window2.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window3
        window3 = Tk()
        radio = StringVar()
        window3.title("questionairre")
        window3["background"] = "white"

        lbl=Label(window3,text="Question 4 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window3,text="Q.4 Who was the first cricketer who smacked 6 sixers in an over?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()


        R1=Radiobutton(window3,text="Garry sobers",font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window3,text="Yuvraj singh",font=("Arial",20),background="White",
        variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
        R3=Radiobutton(window3,text="kireon Pollard",font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)
        R4=Radiobutton(window3,text="Stuard Broad",font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

        label=Label(window3)
        label.pack()

        B1=Button(window3,text="Next",font=("Helvetica",15),command=windowD).pack()
        window3.mainloop()


    def windowB():
        import tkinter as tk
        window1.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window2
        window2 = Tk()
        radio = StringVar()
        window2.title("questionairre")
        window2["background"] = "white"

        lbl=Label(window2,text="Question 3 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window2,text="Q.3 Which cricket Batsmen is currently rated number 1 in T20 cricket?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1=Radiobutton(window2,text="Babar azam",font=("Arial",20),background="White",
        variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window2,text="Sachin Tendulkar",font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)
        R3=Radiobutton(window2,text="Dawid Malan",font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R4=Radiobutton(window2,text="Virat kohli",font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

        label=Label(window2)
        label.pack()

        B1=Button(window2,text="Next",font=("Helvetica",15),command=windowC).pack()
        window2.mainloop()

    def windowA():
        import tkinter as tk
        window.destroy()

        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)


        global window1
        window1 = Tk()
        radio = StringVar()
        window1.title("questionairre")
        window1["background"] = "white"

        lbl=Label(window1,text="Question 2 of 10",font=("Arial",15),
        background="White").pack()

        lbl1=Label(window1,text="Q.2 Which football club does David Beckham play for?",
        font=("Arial",25),background="cyan",compound=LEFT).pack()

        R1=Radiobutton(window1,text="Manchester united",font=("Arial",20),background="White",
        variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
        R2=Radiobutton(window1,text="Liverpool",font=("Arial",20),background="White",
        variable=radio,value="wrong option",command=selection).pack(anchor=NW)
        R3=Radiobutton(window1,text="Real Madrid",font=("Arial",20),background="White",
        variable=radio,value="correct choice",command=selection).pack(anchor=NW)
        R4=Radiobutton(window1,text="Montevideo Wanderers",font=("Arial",20),background="White",
        variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

        label=Label(window1)
        label.pack()

        B1=Button(window1,text="Next",font=("Helvetica",15),command=windowB).pack()
        window1.mainloop()

    import tkinter

    def selection():
        score = 0
        selected = "you have selected " + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)
    window = Tk()
    radio = StringVar()
    window.title("questionairre")
    window["background"] = "white"
    lbl=Label(window,text="Question 1 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window,text="Q.1 Where were the 2002 worldcup finals held?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window,text="Japan and Korea",font=("Arial",20),background="White",
    variable=radio,value="correct choice",command=selection).pack(anchor=NW)
    R2=Radiobutton(window,text="Germany",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R3=Radiobutton(window,text="Scotland",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window,text="Colombia",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window)
    label.pack()

    B1=Button(window,text="Next",font=("Helvetica",15),command=windowA).pack()
    window.mainloop()

def world_quiz_q():
    def windowI():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window8.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
                score += 10
                print(score)
            else:
                score += 0
                print(score)

        global window9
        window9 = Tk()
        radio = StringVar()
        window9.title("questionairre")
        window9['background'] = "White"
        lbl = Label(window9, text="Question 10 of 10", font=("Arial", 15), background="White").pack()
        lbl = Label(window9, text="Q.10 Which is the largest ocean in world?",
                    font=("Arial", 25), background="cyan", compound=LEFT).pack()
        R1 = Radiobutton(window9, text="Atlantic Ocean", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window9, text="Pacific Ocean", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window9, text="Indian Ocean", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window9, text="Arctic Ocean", font=("Arial", 20), background="White", variable=radio, value=" wrong answer",
                         command=selection).pack(anchor=NW)
        label = Label(window9)
        label.pack()
        B1 = Button(window9, text="Next",
                    font=("helvetica", 15)).pack()  
        window9.mainloop()  


    def windowH():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window7.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window8, text="Bahrain", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option ", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window8, text="Iraq", font=("Arial", 20), background="White", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window8, text="Iran", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window8, text="Israel", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window8)
        label.pack()
        B1 = Button(window8, text="Next", font=("helvetica", 15),
                    command=windowI).pack()  
        window8.mainloop()  


    def windowG():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window6.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window7, text="Coorg", font=("Arial", 20), background="White", variable=radio,
                         value="Correct choice", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window7, text="Darjelling", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window7, text="Mumbai", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window7, text="Assam", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window7)
        label.pack()
        B1 = Button(window7, text="Next", font=("helvetica", 15),
                    command=windowH).pack()  
        window7.mainloop()  


    def windowF():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window5.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window6, text="9", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window6, text="1", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window6, text="3", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window6, text="6", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                         command=selection).pack(anchor=NW)
        label = Label(window6)
        label.pack()
        B1 = Button(window6, text="Next", font=("helvetica", 15),
                    command=windowG).pack()  
        window6.mainloop()  


    def windowE():
        import tkinter as tk
        window4.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window5, text="Atlantic Ocean", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window5, text="Pacific Ocean", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window5, text="Indian Ocean", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window5, text="Arctic Ocean", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window5)
        label.pack()
        B1 = Button(window5, text="Next", font=("helvetica", 15),
                    command=windowF).pack()  
        window5.mainloop()


    def windowD():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window3.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window4, text="Australia", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window4, text="Africa", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window4, text="Europe", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window4, text="Russia", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option ", command=selection).pack(anchor=NW)
        label = Label(window4)
        label.pack()
        B1 = Button(window4, text="Next", font=("helvetica", 15),
                    command=windowE).pack()  
        window4.mainloop()  


    def windowC():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window2.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window3, text="Amazon", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window3, text="Congo", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window3, text="Brahamputra", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window3, text="Nile", font=("Arial", 20), background="White", variable=radio,
                         value="wrong option", command=selection).pack(anchor=NW)
        label = Label(window3)
        label.pack()
        B1 = Button(window3, text="Next", font=("helvetica", 15),
                    command=windowD).pack()  # creates a button to move to next window...not linked yet
        window3.mainloop()  # tells python to run the entire code and make a GUI


    def windowB():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window1.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window2, text="1", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                         command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window2, text="11", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                         command=selection).pack(anchor=NW)
        R3 = Radiobutton(window2, text="3", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                         command=selection).pack(anchor=NW)
        R4 = Radiobutton(window2, text="10", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                         command=selection).pack(anchor=NW)
        label = Label(window2)
        label.pack()
        B1 = Button(window2, text="Next", font=("helvetica", 15),
                    command=windowC).pack()  
        window2.mainloop()  


    def windowA():
        import tkinter as tk
        # imports the tkinter module of python which is a GUI
        window.destroy()
        def selection():
            score = 0
            selected = "you have selected " + str(radio.get())
            label.config(text=selected)
            if str(radio.get()) == "correct choice":
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
        R1 = Radiobutton(window1, text="Hawaii", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect option", command=selection).pack(anchor=NW)
        # creates radiobuttons as to be chosenby the user....only one at a time
        R2 = Radiobutton(window1, text="Norway", font=("Arial", 20), background="White", variable=radio,
                         value="correct choice", command=selection).pack(anchor=NW)
        R3 = Radiobutton(window1, text="Iceland", font=("Arial", 20), background="White", variable=radio,
                         value="wrong choice", command=selection).pack(anchor=NW)
        R4 = Radiobutton(window1, text="Detroit", font=("Arial", 20), background="White", variable=radio,
                         value="incorrect choice", command=selection).pack(anchor=NW)
        label = Label(window1)
        label.pack()
        B1 = Button(window1, text="Next", font=("helvetica", 15),
                    command=windowB).pack()  # creates a button to move to next window...not linked yet
        window1.mainloop()  # tells python to run the entire code and make a GUI


    import tkinter as tk


    def selection():
        score = 0
        selected = "you have selected " + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    window = Tk()
    radio = StringVar()
    window.title("questionairre")
    window['background'] = "White"
    lbl = Label(window, text="Question 1 of 10", font=("Arial", 15), background="White").pack()
    lbl = Label(window, text="Q.1 Dead sea is located between which two countries?", font=("Arial", 25), background="cyan",
                compound=LEFT).pack()
    R1 = Radiobutton(window, text="Jordan and Israel", font=("Arial", 20), background="White", variable=radio, value="correct choice",
                     command=selection).pack(anchor=NW)
    # creates radiobuttons as to be chosenby the user....only one at a time
    R2 = Radiobutton(window, text="Jordan and Sudan", font=("Arial", 20), background="White", variable=radio, value="wrong choice",
                     command=selection).pack(anchor=NW)
    R3 = Radiobutton(window, text="Israel and UAE", font=("Arial", 20), background="White", variable=radio, value="incorrect choice",
                     command=selection).pack(anchor=NW)
    R4 = Radiobutton(window, text="UAE and Egypt", font=("Arial", 20), background="White", variable=radio, value="wrong option",
                     command=selection).pack(anchor=NW)
    label = Label(window)
    label.pack()
    B1 = Button(window, text="Next", font=("helvetica", 15),
                command=windowA).pack()  # creates a button to move to next window...not linked yet
    window.mainloop()

def world_quiz():
    import tkinter as tk

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\MANVI\\Desktop\\GeographyQuiz.png")
        img = img.subsample(smp, smp)
        return img

    root=tk.Tk()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)
     
    var1=tk.IntVar()

    root.title("World Geography Quitzie")
    root['background']='White'
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
     
    lbl1 = tk.Label(root, text="Welcome To The World QUIZZ!",font=("Arial",53),background="cyan",compound=tk.CENTER)
    lbl1.pack()
    img = image(1) # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()
     
    B1=tk.Button(root,text="Start the Quiz",font=("Arial",23),command=world_quiz_q,background="White",padx=10,compound=tk.CENTER).pack()
    B1=tk.Button(root,text="Quiz Menu",font=("Arial",23),command=Quiz_Menu,background="White",compound=tk.CENTER).pack()

    root.mainloop()

def food_quiz():
    
    import tkinter as tk

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\MANVI\\Desktop\\Food.png")
        img = img.subsample(smp, smp)
        return img

    root=tk.Tk()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)
     
    var1=tk.IntVar()

    root.title("Foodies Quitzie")
    root['background']='White'
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
     
    lbl1 = tk.Label(root, text="Welcome To The Foodie QUIZZ!",font=("Arial",50),background="cyan",compound=tk.CENTER)
    lbl1.pack()
    img = image(1) # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()
     
    B1=tk.Button(root,text="Start the Quiz",font=("Arial",23),command=food_quiz_q,background="White",padx=10,compound=tk.CENTER).pack()
    B1=tk.Button(root,text="Quiz Menu",font=("Arial",23),command=Quiz_Menu,background="White",compound=tk.CENTER).pack()

    root.mainloop()

def science_quiz():
    
    import tkinter as tk

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\MANVI\\Desktop\\Science.png")
        img = img.subsample(smp, smp)
        return img

    root=tk.Tk()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)
     
    var1=tk.IntVar()

    root.title("Science Wizz Quitzie")
    root['background']='White'
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
     
    lbl1 = tk.Label(root, text="Welcome To The Science Wizz QUIZZ!",font=("Arial",45),background="cyan",compound=tk.CENTER)
    lbl1.pack()
    img = image(1) # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()
     
    B1=tk.Button(root,text="Start the Quiz",font=("Arial",23),command=science_quiz_q,background="White",padx=10,compound=tk.CENTER).pack()
    B1=tk.Button(root,text="Quiz Menu",font=("Arial",23),command=Quiz_Menu,background="White",compound=tk.CENTER).pack()

    root.mainloop()

def sports_quiz():
    import tkinter as tk

    def image(smp):
        img = tk.PhotoImage(file="C:\\Users\\MANVI\\Desktop\\Sportss.png")
        img = img.subsample(smp, smp)
        return img

    root2=tk.Tk()

    menu = tk.Menu()
    menu.add_command(label="Quit", command=root2.destroy)
    root2.config(menu=menu)
     
    var1=tk.IntVar()

    root2.title("Sports Quitzie")
    root2['background']='White'
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
     
    lbl1 = tk.Label(root2, text="Welcome To The Sports QUIZZ!",font=("Arial",50),background="cyan",compound=tk.CENTER)
    lbl1.pack()
    img = image(1) # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()
     
    B1=tk.Button(root2,text="Start the Quiz",font=("Arial",23),command=sports_quiz_q,background="White",padx=10,compound=tk.CENTER).pack()
    B1=tk.Button(root2,text="Quiz Menu",font=("Arial",23),command=Quiz_Menu,background="White",compound=tk.CENTER).pack()

    root.mainloop()

def Quiz_Menu():
    root.destroy()
    import tkinter as tk

    def select():
        sel=var1.get()
        lbl1.configure(text=sel)
    def image(smp):
        img = PhotoImage(file="C:\\Users\\MANVI\\Desktop\\World.png")
        img = img.subsample(smp, smp)
        return img

    root1=Tk()

    menu = Menu()
    menu.add_command(label="Quit", command=root1.destroy)
    root1.config(menu=menu)
     
    var1=IntVar()

    root1.title("Quitzie Menu")
    root1['background']='White'
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
     
    lbl1 = Label(root1, text="Choose your Quiz Topic!",font=("Arial",53),background="cyan",compound=CENTER)
    lbl1.pack()
    img = image(1) # 1=normal, 2=small, 3=smallest
    but.config(image=img)
    but.pack()
     
    B1=Button(root1,text="World Quiz",font=("Arial",23),command=world_quiz,background="White",padx=10).pack(side=LEFT)
    B2=Button(root1,text="Sports Quiz",font=("Arial",23),command=sports_quiz,background="White").pack(side=RIGHT)
    B3=Button(root1,text="Food Quiz",font=("Arial",23),command=food_quiz,background="White",padx=16).pack(side=LEFT)
    B4=Button(root1,text="Science Quiz",font=("Arial",23),command=science_quiz,background="White",compound=CENTER).pack()

    root1.mainloop()


from tkinter import *

def select():
    sel=var1.get()
    lbl1.configure(text=sel)  #used to access object's attributes after initialization
def image(smp):
    img = PhotoImage(file="C:\\Users\\MANVI\\Desktop\\Quizzzzzz.png")
    img = img.subsample(smp)   #Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
    return img

root=Tk()

menu = Menu()
menu.add_command(label="Quit", command=root.destroy)
root.config(menu=menu)
 
var1=IntVar()  #holds integer data

root.title("Damnic Quitzie")
root['background']='White'
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
 
lbl1 = Label(root, text="Welcome To The Quiz!",font=("Arial",55),background="cyan",compound=CENTER)
lbl1.pack()
img = image(1) # 1=normal, 2=small, 3=smallest
but.config(image=img)  #change the property of the widget
but.pack() #make widget fill the entire frame and declares its position
lbl2=Label(root, text="Press enter to begin",font=("Arial",20),background="cyan").pack()

B1=Button(root,text="Enter",font=("Arial",25), relief="groove", background="White",command=Quiz_Menu,compound=CENTER).pack()


root.mainloop()
