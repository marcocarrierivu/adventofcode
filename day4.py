xmas = []
rowList = []
with open("Day 4/input.txt") as file:

    for line in file:
        rowList = []
        for letter in line.strip():
            rowList.append(letter)
        xmas.append(rowList)
    file.close()

# WORKS ON SAMPLE INPUT

# xmas = [
#     [["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["X"], ["M"], ["A"], ["S"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["X"], ["Z"], ["A"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["M"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["X"], ["Z"], ["A"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["Z"], ["Z"], ["S"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]],
#     [["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"], ["Z"]]
# ]


numRows = len(xmas)-1
numCols = len(xmas[0])-1

def checkUpLeft(xmas, row, col, numRows, numCols):
    """
    Return true if it's possible to get the UpLeft diagonal.
    """
    if row >= 3 and col >= 3:
        return True
    else:
        return False
    
def checkUpRight(xmas, row, col, numRows, numCols):
    """
    Return true if it's possible to get the UpRight diagonal.
    """
    if row >= 3 and col <= numCols-3:
        return True
    else:
        return False
    
def checkDownLeft(xmas, row, col, numRows, numCols):
    """
    Return true if it's possible to get the DownLeft diagonal.
    """
    if row <= numRows - 3 and col >=3:
        return True
    else:
        return False
    
def checkDownRight(xmas, row, col, numRows, numCols):
    """
    Return true if it's possible to get the DownRight diagonal.
    """
    if row <= numRows - 3 and col <= numCols - 3:
        return True
    else:
        return False
    
def checkLeft(xmas, row, col, numRows, numCols):
    if col >= 3:
        return True
    else:
        return False
    
def checkRight(xmas, row, col, numRows, numCols):
    if col <= numCols - 4:
        return True
    else:
        return False    
    
def checkUp(xmas, row, col, numRows, numCols):
    if row >= 3:
        return True
    else:
        return False
    
def checkDown(xmas, row, col, numRows, numCols):
    if row <= numRows - 3:
        return True
    else:
        return False

def getUpLeft(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row-i][col-i][0]
    # print(string, "up left")
    return string

def getUpRight(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row-i][col+i][0]
    # print(string, "up right")
    return string

def getDownLeft(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row+i][col-i][0]
    # print(string, "down left")

    return string

def getDownRight(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row+i][col+i][0]
    # print(string, "down right")

    return string

def getLeft(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row][col-i][0]
    # print(string, "left")

    return string

def getRight(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row][col+i][0]
    # print(string, "right")

    return string

def getUp(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row-i][col][0]
    # print(string, "up")
    return string

def getDown(xmas, row, col):
    string = ""
    for i in range(0,4):
        string += xmas[row+i][col][0]
    # print(string, "down")

    return string

xmasCounter = 0

for row in range(numRows+1):
    for col in range(numCols+1):
        # print(xmas[row][col])

        if checkUpLeft(xmas, row, col, numRows, numCols):
            # print(row, col, "check up left")
            if getUpLeft(xmas, row, col) == "XMAS":
                print(row, col, "upleft")
                xmasCounter += 1

        if checkUpRight(xmas, row, col, numRows, numCols):
            # print(row, col, "check up right")

            if getUpRight(xmas, row, col) == "XMAS":
                print(row, col, "upright")
                xmasCounter += 1       

        if checkDownLeft(xmas, row, col, numRows, numCols):
            # print(row, col, "check downleft")

            if getDownLeft(xmas, row, col) == "XMAS":
                print(row, col, "downleft")
                xmasCounter += 1   

        if checkDownRight(xmas, row, col, numRows, numCols):
            # print(row, col, "check downright")

            if getDownRight(xmas, row, col) == "XMAS":
                print(row, col, "downright")
                xmasCounter += 1   

        if checkLeft(xmas, row, col, numRows, numCols):
            # print(row, col, "check left")

            if getLeft(xmas, row, col) == "XMAS":
                print(row, col, "left")
                xmasCounter += 1  

        if checkRight(xmas, row, col, numRows, numCols):
            # print(row, col, "check right")

            if getRight(xmas, row, col) == "XMAS":
                print(row, col, "right")
                xmasCounter += 1  

        if checkUp(xmas, row, col, numRows, numCols):
            # print(row, col, "check up")

            if getUp(xmas, row, col) == "XMAS":
                print(row, col, "up")
                xmasCounter += 1    

        if checkDown(xmas, row, col, numRows, numCols):
            # print(row, col, "check down")

            if getDown(xmas, row, col) == "XMAS":
                print(row, col, "down")
                xmasCounter += 1         
        # print()                                       
 
print(xmasCounter)