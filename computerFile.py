from solver import solve
from generateTable import printTable
from playerFile import enterIndexOrValue, checkValue

def gameComputer():
    table = [[0 for j in range(9)] for i in range(9)]

    print("Ready!")
    printTable(table)

    print("If you're done, just enter 42")

    while True:

        print("Inter index of line:")
        indexLine = enterIndexOrValue()

        if checkValue(indexLine): 
            print("Okey")
            return
        
        print("Inter index of column:")
        indexColumn = enterIndexOrValue()

        if checkValue(indexColumn): 
            print("Okey")
            return

        print("Enter a value:")
        indexToAdd = enterIndexOrValue()

        if checkValue(indexToAdd): 
            print("Okey")
            return
        
        table[indexLine][indexColumn] = indexToAdd + 1

        printTable(table)

    checkTable = solve(table)

    if checkTable == False:
        print("It's impossible")

    else:
        print("Done!")
        printTable(table)