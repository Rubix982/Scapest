string = """
I U L H Q G V K L S

I N T H E R O O M W

H E R E A G I G A N

T I C E V E N T W A

S C A R E D F O R W

A I T S F O R Y O U

A N E V E L O P E T

H A T A N S W E R S

Y O U R Q U E S T I

O N S . T H E K E Y

T O A N S W E R T H

E H O L D E R O F T

H E E N V E L O P E

I S T H E N A M E O

F T H E S T R E E T

Y O U C O M E F R O

M , S H E R L O C K

T H E K E Y F O R T

H E N E X T C I P H

E R I S G A K Q L A
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
    print("", end="\n")