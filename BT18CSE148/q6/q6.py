ini = input('Enter the initials of name in capital : ')
with open('D:\python\demo2.txt', 'r+') as file:
    for line in file:        
        word = line.split()
        if len(word) == 2 and len(ini) == 2 :
            f_ini = word[0][0]
            l_ini = word[1][0]
            if ini[0] == f_ini and l_ini == ini[1]:
                print(*word, sep = "")
        if len(word) == 3 :
            f_ini = word[0][0]
            m_ini = word[1][0]
            l_ini = word[2][0]
            if (ini[0] == f_ini and ini[1] == l_ini) or (ini[0] == f_ini and ini[2] == l_ini and ini[1] == m_ini ):
                print(*word, sep = "")

file.close()