# Use words.txt as the file name
fname = input("Enter file name: ")
#enter file name. please make sure the file is in the same directory as the program
fh = open(fname)
#opens a portal for the file
for line in fh:
    fr= line.rstrip()
    print(fr.upper())
