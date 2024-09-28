fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#making an empty list

for line in fh:
    x = line.strip().split()
    #splitting the line into words
    for i in x:
        if i not in lst:
            lst.append(i)
            #appending the words to the list

print(sorted(lst))
#sorting the list and printing it