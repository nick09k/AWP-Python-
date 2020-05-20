#question 3
with open('D:\python\students.txt', 'r') as file1:
    with open('D:\python\students2.txt', 'w') as file2:
        for line in file1 :
            splitLine=line.split('\t')
            name=splitLine[0]
            split_name = name.split(" ")
            f_name = split_name[0].capitalize()
            l_name = split_name[len(split_name)-1].capitalize()
            name=f_name + " " + l_name
            phoneno="301-"+str[2]
            file2.write(name+"\t"+str[1]+"\t"+phoneno + "\n")
file1.close()
file2.close()