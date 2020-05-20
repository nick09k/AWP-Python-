#question 3
#opening file and increasing value
newDict = {}
with open('D:\python\class_score.txt', 'r') as f:
        for line in f:
            splitLine = line.split()
            newDict[splitLine[0]] = ",".join(splitLine[1:])
        for keys in newDict: 
            newDict[keys] = int(newDict[keys]) + 5   

#saving new details in othe rfile
with open('D:\python\score2.txt', 'w') as f:
    for key, value in newDict.items():
        f.write('%s:%s\n' % (key, value))

f.close()