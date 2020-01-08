infile = "wordscapeswords.txt"
outfile = "wordscapeswordsEdited.txt"
fin = open(infile)
fout = open(outfile, "w+")
to_remove = []
while True:
    query = str(raw_input("Type a word to remove (enter q to exit): "))
    if query == "q":
        break
    else:
        to_remove.append(query)

word_list = []
for line in fin:
    for word in line.split():
        for query in to_remove:
            if word.upper() == query.upper():
                line = line.replace(line, "")
                print query + " removed"
    word_list.append(line)

for line in word_list:
    fout.write(line)
fin.close()
fout.close()
