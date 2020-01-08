from itertools import chain, permutations

def findWord(words, left, right, query):
    if right >= left:
        mid = (left + right)/2
        if words[mid] == query:
            return mid
        elif words[mid] > query:
            return findWord(words, left, mid - 1, query)
        else:
            return findWord(words, mid + 1, right, query)
    else:
        return -1

print "Welcome to Wordscapes Word Finder"
while True:
    letters = raw_input("Enter letters: ")
    if len(letters) < 3:
        print "Please enter at least 3 letters"
    else:
        break
wordList = []

"""Erases words less than 3 letters from file scrabblewords.txt"""
# def eraseSmallWords():
#     infile = "wordscapeswordsBackup.txt"
#     outfile = "wordscapeswordsBackup2.txt"
#     fin = open(infile)
#     fout = open(outfile, "w+")
#     for line in fin:
#         if len(line) < 5:
#             line = line.replace(line, "")
#         fout.write(line)
#     fin.close()
#     fout.close()
# eraseSmallWords()

print "Calculating..."
with open("wordscapeswords.txt", "r") as wordfile:
    for line in wordfile:
        for word in line.split():
            if (len(word) >= 3):
                wordList.append(word)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(permutations(s, r) for r in range(len(s)+1))

letterList = list(map(''.join, powerset(letters)))

finalwords = []
for word in letterList:
    found = findWord(wordList, 0, len(wordList) - 1, word.upper())
    if found != -1:
        finalwords.append(word)
    # for validword in wordList:
    #     if word.upper() == validword:
    #         finalwords.append(word)
finalwords = list(set(finalwords)) # check for duplicates
finalwords.sort()
finalwords.sort(key = len, reverse = True)
words3 = []
for word in reversed(finalwords):
    if len(word) == 3:
        finalwords.remove(word)
        words3.append(word)

print "4+ letter words: "
print finalwords
print "3 letter words: "
print list(reversed(words3))
