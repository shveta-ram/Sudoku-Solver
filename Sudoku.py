sudoku = [[0, 3, 4, 0], [4, 0, 0, 2], [1, 0, 0, 3], [0, 2, 1, 0]] # sample unsolved sudoku
sudokuColumn = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]

for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        print(sudoku[i][j], end=' ')
    print()

print()

findNumber = []
fourByFour = {1, 2, 3, 4}
for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        if sudoku[i][j] == 0:
            findNumber = sudoku[i] + sudokuColumn[j]  # concatenates the row and column
            print(findNumber)
            findNumber = [x for x in findNumber if x != 0]  # extracts the non zero numbers
            findNumber = set(findNumber)  # gets the set of non zero numbers to rid of duplicates
            number = fourByFour.difference(findNumber)  # uses set identities to find numbers in 4x4 not in sudoku
            number = number.pop()  # removes the 0
            sudoku[i][j] = number  # adds new number

for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        print(sudoku[i][j], end=' ')
    print()
























