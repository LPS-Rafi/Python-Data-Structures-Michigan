fname = input("Enter file name: ")
fh = open(fname)
count=0

for line in fh:
    if line.startswith("From:"):
        continue
    #skip the line that starts with "From:"
    if line.startswith("From"):
        psudo = line.rstrip().split()[1]
        #splitting the line into words and taking the second word
        print(psudo)
        count+=1

print("There were", count, "lines in the file with From as the first word")