infile = "wordscapeswords.txt"
fin = open(infile)
count = 0
for line in fin:
    count += 1
print ("There are " + str(count) + " words")
