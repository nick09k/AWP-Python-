#question11
def printTable():
        tableData=[['apples','oranges','cherries','banana'],
                  ['Alpha','Beta','Gamma','Delta'],
                  ['dogs','cats','moos','goos']]
        
        i= 0
        j=0
        while i <4:
            word = " "
            while j <= 2:
                word = word + " " +  tableData[j][i]
                j+=1
            i+=1
            j=0
            print(word)
              
printTable()