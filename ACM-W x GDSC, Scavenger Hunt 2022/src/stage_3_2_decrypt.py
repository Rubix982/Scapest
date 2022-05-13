string = """
S L K V Q G H L U I

W M O O E R H T N I

N A G I A G E R E H

A W T N V E E C I T

W R O F E D R A C S

U O Y R F O S T I A

T E P O E L V E N A

S R E W N S A T A H

I T S E Q U R U O Y

Y E K E T H . S N O

H T R E S W N A O T

T F O R D E L O H E

E P O L V E N E E H

O E M A E N H T S I

T E E R S T E H T F

O R F E O M C U O Y

K C O L E R H S , M

T R O F E Y K E H T

H P I C X T E N E H

A L Q K G A S I R E
"""

string = string.split('\n')[1:-1]
stringClean = []

for line in string:
    if line != '':
        stringClean.append(line)

lines = []
matrix = []

for line in stringClean:
    lines.append(line.split(' '))

for i in range(0, len(lines[0])):
    tempArr = []
    for j in range(0, len(lines)):
        tempArr.append(lines[j][i])
    matrix.append(tempArr)

for i in range(0, len(matrix)//2 + 1):
    temp_list = matrix[i]
    matrix[i] = matrix[len(matrix) - 1 - i]
    matrix[len(matrix) - 1 - i] = temp_list

for i in range(0, len(matrix)):
    if len(matrix[i]) == 8:
        print(matrix[i], i)

for i in range(0, len(matrix[0])):
    for j in range(0, len(matrix)):
        print(matrix[j][i], end=" ")
    print("")
