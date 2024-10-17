name = input("Enter file:")
handle = open(name)

storage = {}
for lines in handle:
    if lines.startswith("From "):
        temp=lines.strip().split()[1]
        storage[temp] = storage.get(temp,0)+1
            
bigValue=None
bigName=None

for keys in storage.keys():
    if bigValue is None or bigValue<storage[keys]:
        bigValue = storage[keys]
        bigName = keys
        
print(bigName, bigValue)