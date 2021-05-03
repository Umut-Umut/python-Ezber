from database import loadData, checkData, writeData
from tkinter import END
from random import randint, choice

enWordsDict = {}
trWordsDict = {}

for i in loadData():
    enWord = i[0]
    trWord = i[1]
    enWordsDict[enWord] = trWord
    trWordsDict[trWord] = enWord

ent1Text = "İngilizce kelime."
ent2Text = "Karşılığı veya yeni anlamı."
falseTextC = "#da2400"
trueTextC = "#176c09"

# FUNCTIONS
def feedback(label, textParam, fgParam=falseTextC):
    label.config(text=textParam, fg=fgParam)
    label.after(3000, lambda: label.config(text="---", fg="black"))


def addListbox(listboxParam, textParam, fgParam=trueTextC):
    listboxParam.insert(0, textParam)
    listboxParam.itemconfig(0, fg=fgParam)


def startAsk(labelParam1, labelParam2, listboxParam, entryParam, windowParam):
    askWord, index = ask()
    labelParam1.config(text=askWord)    

    def check():
        def result(resultParam):
            if resultParam:
                feedback(labelParam2, "Doğru", trueTextC)    
                addListbox(listboxParam, f"{askWord}: {userWord}")
            else:
                feedback(labelParam2, "Yanlış")
                whichDict = enWordsDict if index == 0 else trWordsDict
                addListbox(listboxParam, f"{askWord}: {whichDict[askWord]} --> {userWord}", falseTextC)


        userWord = entryParam.get().lower()
        if len(userWord) == 0:
            feedback(labelParam2, "Kelime anlamı girilmedi!")
        else:
            if index:
                result(1) if userWord == trWordsDict[askWord] else result(0)
            else:
                result(1) if userWord == enWordsDict[askWord] else result(0)

            entryParam.select_to(END)
            entryParam.focus()

            startAsk(labelParam1, labelParam2, listboxParam, entryParam, windowParam)

    entryParam.focus()
    windowParam.bind("<Return>", lambda e: check())


def ask():
    dictLists = [enWordsDict, trWordsDict]

    index = randint(0,1)
    choicedDict = dictLists[index]

    dictKeysList = list(choicedDict.keys())

    choicedWord = choice(dictKeysList)

    return choicedWord, index


def getEntry(entryParam1, entryParam2):
        enWord = entryParam1.get().lower()
        trWord = entryParam2.get().lower()
        return enWord, trWord


def check(labelParam, entryParam1, entryParam2):
    enWord, trWord = getEntry(entryParam1, entryParam2)
    if len(enWord) == 0 or len(trWord) == 0:
        feedback(labelParam, "Boş kısımlar var!")

    elif enWord == "i̇ngilizce kelime." or trWord == "karşılığı veya yeni anlamı.":
        feedback(labelParam, "Anlam veya kelime girilmedi!")

    elif not((enWord.replace(" ", "")).isalpha() and (trWord.replace(" ", "")).isalpha()):
        feedback(labelParam, "Yalnızca harf olmalı!")

    else:
        return 1


def wordReMeaning():
    pass


def recordingWord(labelParam, entryParam1, entryParam2, listboxParam):
    if check(labelParam, entryParam1, entryParam2):
        enWord, trWord = getEntry(entryParam1, entryParam2)
        if checkData(enWord) or enWord in enWordsDict.keys():
            translate = enWordsDict[enWord]
            
            feedback(labelParam, f"Bu kelime {translate} olarak kayıtllı.")
            addListbox(listboxParam, f"{enWord}: {translate} --> {trWord}", falseTextC)

            entryFocus(entryParam1)

        else:
            enWordsDict[enWord] = trWord
            trWordsDict[trWord] = enWord

            feedback(labelParam, f"{enWord} kaydedildi", trueTextC)

            entryClear(entryParam1, entryParam2)
            entryParam1.focus()
            addListbox(listboxParam, f"{enWord}: {trWord}")         


def entryFocus(entryParam):
        entryParam.select_to(END)
        entryParam.focus()

        
def entryClear(entryParam1, entryParam2):
    entryParam1.delete(0, END)
    entryParam2.delete(0, END)


def entryWrite(entryParam1, entryParam2):
    entryParam1.insert(0, ent1Text)
    entryParam2.insert(0, ent2Text)


def exitProgram(winParam):
    winParam.destroy()
    for key, value in enWordsDict.items():
        if not checkData(key):
            writeData(key, value)
        else:
            continue
