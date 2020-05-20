#question 8
word = input('Enter a word: ')
charctr = input('Enter a character: ')
flag = 1
for i in range(0,len(word)):
    if word[i] == charctr:
        print(word[:i+1])
        print(word[i+1:])
        flag = 1
        break
    i+=1
if flag == 0:
    print('No such character present in the given string”')