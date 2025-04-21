from tkinter import Frame, Image, Tk, Label, Button, Entry, PhotoImage, Toplevel, Listbox
from main import enWordsDict, trWordsDict, entryFocus, entryWrite, exitProgram, recordingWord,  startAsk, exitProgram

# GLOBAL VARIABLE
fontVariable = "URW 11"
buttonBg = "#5B443E"
buttonBd = 0
backGroundColor =   "#CFA987"#CFA987
# hgVariable =        "#375C32"#375C32
activeBgValue =     "#375C32"#375C32
ListBbackGround =   "#e7bd98"#e7bd98

# MAIN INTERFACE
mainWin = Tk()
mainWin.title("EZBERLE!!!")
mainWin.geometry("300x300")
mainWin.configure(bg=backGroundColor)
mainWin.resizable(width=False, height=False)

#IMAGES
icon = PhotoImage(file="media/e.png")
query = PhotoImage(file="media/query.png")
oldPapper = PhotoImage(file="media/oldPapper.png")
settingsImage = PhotoImage(file="media/cark.png")

mainWin.iconphoto(False, icon)

# FRAMES
fr1 = Frame(mainWin)

# LABELS
lb1 = Label(mainWin, text="---", font=fontVariable, bg=backGroundColor)
# lb1 = Label(mainWin, text="---", font=fontVariable, bg=backGroundColor, highlightcolor=hgVariable)
lb2 = Label(mainWin, text="---", font=fontVariable, bg=backGroundColor)
# lb2 = Label(mainWin, text="---", font=fontVariable, bg=backGroundColor, highlightcolor=hgVariable)

# ENTRYS
ent1 = Entry(mainWin, width=35, justify="center", font=fontVariable, bg=backGroundColor, selectbackground="#FAEDCA")
# ent1 = Entry(mainWin, width=35, justify="center", font=fontVariable, bg=backGroundColor, highlightcolor=backGroundColor, selectbackground="#FAEDCA")

# LISTBOX
listbox = Listbox(mainWin, width=35, height=12, font="URW 11", bg=ListBbackGround, justify="center", activestyle="none")
# listbox = Listbox(mainWin, width=35, height=12, font="URW 11", bg=ListBbackGround, highlightcolor=hgVariable, justify="center", activestyle="none")

# FUNCTIONS
def info():
    infoWin = Toplevel()
    infoWin.title("Hakkında")
    infoWin.iconphoto(False, icon)

    Label(infoWin, image=oldPapper).pack()


def wordOp():
    # SECOND INTERFACE
    secondWin = Toplevel(bg=backGroundColor)
    secondWin.transient(mainWin)
    secondWin.geometry("300x300")
    secondWin.resizable(width=False, height=False)
    secondWin.iconphoto(False, icon)
    #secondWin.configure(bg=)

    # SECOND FRAME
    secondFrame = Frame(secondWin, bg=backGroundColor)

    # SECOND LABELS
    # secondLabel1 = Label(secondWin, text="---", bg=backGroundColor, highlightcolor=hgVariable, font=fontVariable)
    secondLabel1 = Label(secondWin, text="---", bg=backGroundColor, font=fontVariable)

    # SECOND ENTRYS
    secondEnt1 = Entry(secondWin, width=35, justify="center", font=fontVariable, bg=backGroundColor, highlightcolor=backGroundColor, selectbackground="#FAEDCA")
    secondEnt2 = Entry(secondWin, width=35, justify="center", font=fontVariable, bg=backGroundColor, highlightcolor=backGroundColor, selectbackground="#FAEDCA")

    # SECOND LISTBOX
    # secondListbox = Listbox(secondWin, width=35, height=12, font="URW 11", bg=ListBbackGround, highlightcolor=hgVariable, justify="center", activestyle="none")
    secondListbox = Listbox(secondWin, width=35, height=12, font="URW 11", bg=ListBbackGround, justify="center", activestyle="none")
    
    # SECOND LOSTBOX
    secondWin.bind("<Escape>", lambda e: secondWin.destroy())
    secondWin.bind("<Return>", lambda e: recordingWord(secondLabel1, secondEnt1, secondEnt2, secondListbox))

    # SECOND BUTTONS
    secondButton1 = Button(secondFrame, text="Tamam", width=8, bd=buttonBd, font=fontVariable, activebackground=activeBgValue, bg=buttonBg, command=lambda: recordingWord(secondLabel1, secondEnt1, secondEnt2, secondListbox))
    secondButton2 = Button(secondFrame, text="Değiş", state="disable", width=8, bd=buttonBd, font=fontVariable, activebackground=activeBgValue, bg=buttonBg)
    secondButton3 = Button(secondFrame, text="Geri", width=8, bd=buttonBd, font=fontVariable, activebackground=activeBgValue, bg=buttonBg, command=secondWin.destroy)

    # SECOND CORDİNATE
    secondEnt1.pack()
    secondEnt2.pack()

    secondLabel1.pack()

    secondButton1.pack(side="left")
    secondButton2.pack(side="left")
    secondButton3.pack(side="left")

    secondFrame.pack()

    secondListbox.pack()

    entryWrite(secondEnt1, secondEnt2)
    entryFocus(secondEnt1)

# BIND FUNCTION
mainWin.bind("<Escape>", lambda e: exitProgram(mainWin))

# BUTTONS
bt1 = Button(fr1, text="Geç", width=8, bd=buttonBd, font=fontVariable, activebackground=activeBgValue, bg=buttonBg)
bt2 = Button(fr1, text="İşlemler", width=8, bd=buttonBd, font=fontVariable, activebackground=activeBgValue, bg=buttonBg)
bt3 = Button(fr1, text="Çıkış", width=8, bd=buttonBd, activebackground=activeBgValue, bg=buttonBg, font=fontVariable)
bt4 = Button(image=query, bd=buttonBd, activebackground=activeBgValue, bg=buttonBg)
bt5 = Button(image=settingsImage, bd=buttonBd, activebackground=activeBgValue, bg=buttonBg, state="disable")

# BUTTON COMMANDS
bt1.configure(command=lambda: startAsk(lb1, lb2, listbox, ent1, mainWin))
bt2.configure(command=wordOp)
bt3.configure(command=lambda: exitProgram(mainWin))
bt4.configure(command=info)
"""bt5.configure()"""

# OBJECT POSITION
lb1.pack()

ent1.pack()

lb2.pack()

bt1.pack(side="left")
bt2.pack(side="left")
bt3.pack(side="left")

fr1.pack()

listbox.pack()

bt4.place(x=278, y=0)
bt5.place(x=256, y=0)
    
if len(enWordsDict.keys()) == 0:
    en = "rote"
    tr = "ezber"
    enWordsDict[en] = tr
    trWordsDict[tr] = en
    startAsk(lb1, lb2, listbox, ent1, mainWin)
    mainWin.mainloop()
else:
    startAsk(lb1, lb2, listbox, ent1, mainWin)
    mainWin.mainloop()
