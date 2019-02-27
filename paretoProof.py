from collections import Counter

numOfData = int(input("How many documents would you like to scan? (Up to 10): "))

i = 0
displayedI = str(i)

docList = []
finalData = []

while i < numOfData:
    newAddress = input("Address of document " + displayedI + ": ")
    docList.append(newAddress)
    i += 1
    displayedI = str(i)

fname = newAddress
 
num_words = 0
 


    
for idx, x in enumerate(docList):
    with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
    file = open(docList[idx], 'r')
    data_set = file.read().strip()
    file.close()
    split_set = data_set.split()
    CounterVariable = Counter(split_set)
    most_occuring = CounterVariable.most_common(Math.floor(.2 * num_words))
    finalData.append(most_occuring)


if len(docList) < 1:
    doc1 = finalData
    print(doc1)

elif len(docList) == 1:
    doc1 = finalData[0]
    doc2 = finalData[1]
    print(doc1)
elif len(docList) == 2:
    doc1 = finalData[0]
    doc2 = finalData[1]
    doc3 = finalData[2]
    print(doc1, doc2, doc3)
elif len(docList) == 2:
    doc1 = finalData[0]
    doc2 = finalData[1]
    doc3 = finalData[2]
    doc4 = finalData[3]
    print(doc1, doc2, doc3, doc4)
elif len(docList) == 3:
    doc1 = finalData[0]
    doc2 = finalData[1]
    doc3 = finalData[2]
    doc4 = finalData[3]
    doc5 = finalData[4] 
    print(doc1, doc2, doc3, doc4, doc5)
elif len(docList) == 4:
    doc1 = finalData[0]
    doc2 = finalData[1]
    doc3 = finalData[2]
    doc4 = finalData[3]
    doc5 = finalData[4] 
    doc6 = finalData[5]
    print(doc1, doc2, doc3, doc4, doc5, doc6)
else: 
    print("You have selected to many documents")




