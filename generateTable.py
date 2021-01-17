from random import randint
from solver import solve
from copy import copy, deepcopy

def initTable():
    initialLine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    variableLine = initialLine
    table = []
    table.append(initialLine)

    for i in range(1, 9):

        if i % 6 == 0:
            variableLine = initialLine[2:] + initialLine[:2]
            table.append(variableLine)

        elif i % 3 == 0:
            variableLine = initialLine[1:] + [initialLine[0]]
            table.append(variableLine)

        else:
            variableLine = variableLine[3:] + variableLine[:4]
            table.append(variableLine)

    return table

def printTable(table):
    for i in range(len(table)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(table[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(table[i][j])
            else:
                print(str(table[i][j]) + " ", end="")

def transpositionMatrix(table):
    table = [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]

    return table

def swapColumns(table):
    firstColumn = randint(0, 8)
    secondColumn = randint(0, 8)

    while firstColumn == secondColumn:
        secondColumn = randint(0, 8)

    for i in range(len(table)):
        table[i][firstColumn], table[i][secondColumn] = table[i][secondColumn], table[i][firstColumn]

    return table

def swapLines(table):
    table = transpositionMatrix(table)
    table = swapColumns(table)
    table = transpositionMatrix(table)

    return table

def swapLinesInArea(table):
    idArea = randint(0, 2)
    firstLine = randint(0, 2) + idArea * 3
    secondLine = randint(0, 2) + idArea * 3

    while firstLine == secondLine:
        secondLine = randint(0, 2) + idArea * 3

    table[firstLine], table[secondLine] = table[secondLine], table[firstLine]

    return table

def swapColumnsInArea(table):
    table = transpositionMatrix(table)
    table = swapLinesInArea(table)
    table = transpositionMatrix(table)

    return table

def generateRandomTable():
    table = initTable()

    arrayFunctions = [
        "transpositionMatrix(table)",
        "swapColumns(table)",
        "swapLines(table)",
        "swapLinesInArea(table)",
        "swapColumnsInArea(table)"
    ]

    for i in range(15):
        idTransformation = randint(0, 4)
        table = eval(arrayFunctions[idTransformation])

    return table

def deleteCell(table):
    flook = [[0 for j in range(9)] for i in range(9)]

    for i in range(3 ** 4):
        iIndex = randint(0, 8)
        jIndex = randint(0, 8)

        if flook[iIndex][jIndex] == 0:
            flook[iIndex][jIndex] = 1

            temp = table[iIndex][jIndex]
            table[iIndex][jIndex] = 0

            copyTable = deepcopy(table)

            if solve(copyTable) == False:
                table[iIndex][jIndex] = temp

    return table

def generateTable():
    table = deleteCell(generateRandomTable())

    return table