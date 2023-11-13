import time
import csv
import multiprocessing
import matplotlib.pyplot as plt

def read_matrix(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        matrix = list(reader)
        for i in range(len(matrix)):
            matrix[i] = [int(x) for x in matrix[i]]
    return matrix

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время: {end_time - start_time} секунд")
        return result
    return wrapper

@timer
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

@timer
def parallel_matrix_multiplication(matrix1, matrix2, num_processes):
    result = []
    with multiprocessing.Pool(processes=num_processes) as pool:
        result = pool.starmap(multiply_matrices, [(matrix1, matrix2)])
    return result


matrix1 = read_matrix('/Users/polinalihaceva/Desktop/homework/matrix_1.csv')
matrix2 = read_matrix('/Users/polinalihaceva/Desktop/homework/matrix_2.csv')

times = []
for i in range(1, 6):
    start_time = time.time()
    parallel_matrix_multiplication(matrix1, matrix2, i)
    end_time = time.time()
    times.append((end_time - start_time))

num_processes = list(range(1, 6))
plt.plot(num_processes, [times[0]/t for t in times], marker='o')
plt.xlabel('Number of processes')
plt.ylabel('T1 / Tn')
plt.show()