#question 9
word_list = []
word1= input('Enter string One: ')
word2 = input('Enter string second :')
if len(word1) == len(word2):
    i = 0
    while i<len(word1):
        #
        word_list.append(word1[i])
        word_list.append(word2[i])
        i+=1
    print(*word_list, sep = "") 
else:
    print('Strings are not of same length so exiting the program')