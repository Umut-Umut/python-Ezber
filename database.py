from sqlite3 import connect

with connect("word.bank") as db:
    cs = db.cursor()

    def createTable():
        cs.execute("CREATE TABLE IF NOT EXISTS wordBank(english, turkish)")


    def writeData(englishWord, turkishWord):
        cs.execute("INSERT INTO wordBank VALUES(?, ?)", (englishWord.lower(), turkishWord.lower()))
        db.commit()


    def loadData(column="*"):
        return cs.execute("SELECT {} FROM wordBank".format(column)).fetchall()

    def checkData(word, column=0):
        lang = "turkish" if column == 1 else "english"
        try:
            cs.execute(f"SELECT {lang} FROM wordBank WHERE {lang} = '{word}'").fetchone()[0]
            return 1
        except:
            return 0


    def updateData():
            pass

createTable()
