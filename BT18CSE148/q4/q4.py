#question 4
#using list to store marks
grade = 0
print('Enter the passing marks')
rqd = int(input())
with open('D:\python\demo.txt', 'r') as f:
        for line in f:
            grade = 0
            splitLine = line.split()
            for i in range(1,len(splitLine)):
                splitLine[i] = int(splitLine[i])
            for i in range(1,len(splitLine)):
                grade += splitLine[i]
            if rqd<= grade:
                print(splitLine[0] + ' has passed. ')
                print(grade)
            else:
                print(splitLine[0] + ' has failed. ')
                print(grade)
f.close()