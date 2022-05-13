matrix = [['T', 'G', 'K', 'A', 'V', 'O', 'E', 'I', 'C', 'T', 'H', 'E'], ['W', 'P', '6', 'T', 'E', 'M', 'M', 'E', 'I', 'H', 'E', 'R'], ['E', 'E', 'K', 'I', 'R', 'P', 'E', 'N', 'T', 'E', 'N', 'I'], ['N', 'C', 'A', 'O', 'S', 'U', 'R', 'C', 'Y', 'K', 'E', 'S'], ['T', 'H', 'R', 'N', 'I', 'T', 'G', 'E', 'C', 'E', 'X', 'G'], ['Y', 'S', 'A', 'A', 'T', 'E', 'I', 'S', 'A', 'Y', 'T', 'A'], ['T', 'B', 'C', 'L', 'Y', 'R', 'N', 'F', 'M', 'F', 'C', 'K'], ['W', 'L', 'H', 'U', 'O', 'A', 'G', 'A', 'P', 'O', 'I', 'Q'], ['O', 'O', 'I', 'N', 'F', 'N', 'S', 'S', 'U', 'R', 'P', 'L'], ['-', 'C', 'N', 'I', 'C', 'D', 'C', 'T', 'S', 'T', 'H', 'A']]

for i in range(0, len(matrix)//2 + 1):
    temp_list = matrix[i]
    matrix[i] = matrix[len(matrix) - 1 - i]
    matrix[len(matrix) - 1 - i] = temp_list

for i in range(0, len(matrix)):
#    print(len(matrix[i]))

    if len(matrix[i]) == 8:
        print(matrix[i], i)

for i in range(0, len(matrix[0])):
    for j in range(0, len(matrix)):
        print(matrix[j][i], end=" ")
    print("")

# print(matrix)
