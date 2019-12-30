infile = "wordscapeswords.txt"
outfile = "wordscapeswordsEdited.txt"
fin = open(infile)
fout = open(outfile, "w+")
while True:
    query = str(raw_input("Type a word to remove (enter q to exit): "))
    if query == "q":
        break
    for line in fin:
        for word in line.split():
            if word.upper() == query.upper():
                line = line.replace(line, "")
                print "removed"
            fout.write(line)
fin.close()
fout.close()
