#question 10
import re

with open('D:\python\sentence.txt', 'r') as f:
    flag = 0
    regex = '^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$'
    for line in f:
        line.strip()
        match=re.search(regex,line,re.IGNORECASE)
        if match != None:
            print(match[0])
            flag = 1
    if flag == 0:
            print('No Match Found')

f.close()