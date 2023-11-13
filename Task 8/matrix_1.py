import csv

def read_matrix(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        matrix = list(reader)
        for i in range(len(matrix)):
            matrix[i] = [int(x) for x in matrix[i]]
    return matrix

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

matrix1 = read_matrix('/Users/polinalihaceva/Desktop/homework/matrix_1.csv')
matrix2 = read_matrix('/Users/polinalihaceva/Desktop/homework/matrix_2.csv')
result = multiply_matrices(matrix1, matrix2)
print(result)
