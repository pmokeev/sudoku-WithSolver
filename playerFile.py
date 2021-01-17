from generateTable import generateTable, printTable

def countZero(table):
    count = 0

    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                count += 1

    return count

def checkValue(value):
    return value == 41

def enterIndexOrValue():
    while True:
            try:
                index = int(input())

            except:
                print("Something went wrong! Let's try again.")
                continue

            if index >= 1 and index <= 9 or index == 42:
                index -= 1
                return index
            else:
                print("Try again!")

def gamePlayer():
    table = generateTable()

    printTable(table)

    print("If you are tired, just enter 42")
    
    while countZero(table) != 0:

        print("Inter index of line:")
        indexLine = enterIndexOrValue()

        if checkValue(indexLine): 
            print("Have a nice day!")
            return
        
        print("Inter index of column:")
        indexColumn = enterIndexOrValue()

        if checkValue(indexColumn): 
            print("Have a nice day!")
            return

        print("Enter a value:")
        indexToAdd = enterIndexOrValue()

        if checkValue(indexToAdd): 
            print("Have a nice day!")
            return

        table[indexLine][indexColumn] = indexToAdd + 1

        printTable(table)

    print("You win!")