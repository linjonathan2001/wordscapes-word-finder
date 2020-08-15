print ("Welcome to Wordscapes Word Finder")
while True:
    letters = input("Enter letters: ")
    if len(letters) < 3:
        print ("Please enter at least 3 letters")
    else:
        break
wordList = []

print ("Calculating...")
with open("wordscapeswords.txt", "r") as wordfile:
    for line in wordfile:
        for word in line.split():
            wordList.append(word)

charCount = []
for i in range(0, 26):
    charCount.append(0)

for letter in letters:
    if (letter >= 'a' and letter <= 'z'):
        charCount[ord(letter) - ord('a')] += 1

finalWords = []
tempCount = []

for word in wordList:
    tempCount = charCount.copy()
    valid = True
    for letter in word:
        if (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
            tempCount[ord(letter) - ord('A')] -= 1
            if (tempCount[ord(letter) - ord('A')] < 0):
                valid = False
    if valid:
        finalWords.append(word)

print(finalWords)
