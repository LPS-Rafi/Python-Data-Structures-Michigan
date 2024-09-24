# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

sumation= 0.0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #checking if the line is the one we are looking for
    colon_posi = line.find(":")
    #finding the position of the colon
    num = float(line[colon_posi+1:].strip())
    #extracting the number from the line and converting it to a float
    sumation += num
    count += 1

avg= sumation/count
#calculating the average
print("Average spam confidence:",avg)