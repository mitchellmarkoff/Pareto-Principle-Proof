from collections import Counter

numOfData = int(input("How many documents would you like to scan? "))

i = 0
displayedI = str(i)

docList = []
finalData = []

while i < numOfData:
    newAddress = input("Address of document " + displayedI + ": ")
    docList.append(newAddress)

    i += 1
    displayedI = str(i)

print(docList)
indexList = 0

for idx, x in enumerate(docList):
    file = open(docList[idx], 'r')
    data_set = file.read().strip()
    file.close()
    split_set = data_set.split()
    CounterVariable = Counter(split_set)
    most_occuring = CounterVariable.most_common(20)
    finalData.append(most_occuring)

    
print(finalData)

