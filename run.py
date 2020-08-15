from tkinter import *

def main():
  setup_gui()

def find(l, lb, lb2, event = None):
    lb.delete(0, "end")
    lb2.delete(0, "end")
    letters = []
    letters = l
    maxLength = len(letters)
    wordList = []

    with open("words.txt", "r") as wordfile:
        for line in wordfile:
            for word in line.split():
                wordList.append(word)

    charCount = []
    for i in range(0, 26):
        charCount.append(0)

    for letter in letters:
        if (letter >= 'a' and letter <= 'z'):
            charCount[ord(letter) - ord('a')] += 1
        if (letter >= 'A' and letter <= 'Z'):
            charCount[ord(letter) - ord('A')] += 1

    finalWords = []
    tempCount = []

    for word in wordList:
        if len(word) <= maxLength:
            tempCount = charCount.copy()
            valid = True
            for letter in word:
                if (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
                    tempCount[ord(letter) - ord('A')] -= 1
                    if (tempCount[ord(letter) - ord('A')] < 0):
                        valid = False
            if valid:
                finalWords.append(word.lower())

    finalWords.sort()
    finalWords.sort(key = len, reverse = True)
    words3 = []
    for word in reversed(finalWords):
        if len(word) == 3:
            finalWords.remove(word)
            words3.append(word)

    i = 0
    j = 0
    if len(finalWords) == 0:
        lb.insert(0, "No words found")
    if len(words3) == 0:
        lb2.insert(0, "No words found")
    for word in finalWords:
        lb.insert(i, word)
        i += 1
    for word in reversed(words3):
        lb2.insert(j, word)
        j += 1

def assignDelete(event, word, mylist):
    word = mylist.get(mylist.curselection())
    print(word.upper())

def delete(lb):
    infile = "words.txt"
    outfile = "wordsEdited.txt"
    fin = open(infile)
    fout = open(outfile, "w+")
    query = lb.get(lb.curselection())

    word_list = []
    for line in fin:
        for word in line.split():
            if word.upper() == query.upper():
                line = line.replace(line, "")
                print (query + " removed")
        word_list.append(line)

    for line in word_list:
        fout.write(line)
    fin.close()
    fout.close()

    import os
    os.remove("words.txt")
    os.rename("wordsEdited.txt", "words.txt")
    lb.delete(lb.curselection())

def setup_gui():
    # GUI
    window = Tk()
    window.title('Wordscapes Word Finder')
    entryLabel = Label(window, text = 'Letters: ')
    entryLabel.pack()

    # entry box
    entry = Entry(window)
    entry.pack()

    # 3 letter words
    frame2 = Frame(window)
    frame2.pack(side = BOTTOM)
    scrollbar2 = Scrollbar(frame2)
    scrollbar2.pack(side = RIGHT, fill = Y)
    mylist2 = Listbox(frame2, width = 50, height = 10, yscrollcommand = scrollbar2.set )
    scrollbar2.configure(command = mylist2.yview)
    mylist2.pack(fill = BOTH, side = BOTTOM)

    frame3 = Frame(window)
    frame3.pack(side = BOTTOM)
    label2 = Label(frame3, text = '3 letter words: ')
    label2.pack(side = LEFT)

    # 4 letter words
    frame = Frame(window)
    frame.pack(side = BOTTOM)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(frame, width = 50, height = 15, yscrollcommand = scrollbar.set )
    scrollbar.configure(command = mylist.yview)
    mylist.pack(fill = BOTH, side = BOTTOM)

    frame4 = Frame(window)
    frame4.pack(side = BOTTOM)
    label1 = Label(frame4, text = '4+ letter words: ')
    label1.pack(side = LEFT)

    # button
    findWords = Button(window, text = 'Find Words', command = lambda: find(entry.get(), mylist, mylist2))
    findWords.pack(side = TOP)
    window.bind('<Return>', lambda event = None: findWords.invoke())

    dWord = StringVar
    mylist.bind('<<ListboxSelect>>', lambda event = None: assignDelete(event, dWord, mylist))
    deleteWord = Button(window, text = 'Remove Selected Word', command = lambda: delete(mylist))
    deleteWord.pack(side = BOTTOM)
    window.bind('<BackSpace>', lambda event = None: deleteWord.invoke())

    window.mainloop()

if __name__ == "__main__":
    main()