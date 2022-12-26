
numbers = 10
for rowIndex in range(numbers):
    rowString = ''
    for columnIndex in range(numbers): #Same number of points
        #each row is equivalent to the previous row + 1 - use existing iterator
        rowString += str(columnIndex + rowIndex) + '\t'
    print(rowString)


