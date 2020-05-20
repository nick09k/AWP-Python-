#question 5
import os,glob,re
flag = 0
folder_path = 'D:/python'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(filename, 'r') as f:
        for x in f:
            date = re.compile(r'python')
            match = date.search(f.readline())
            if match!=None:
                print('Match  Found : ')
                print (filename)
                flag = 1 
                
if flag == 0:
    print('No such file')
f.close()