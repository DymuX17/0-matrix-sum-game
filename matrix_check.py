import numpy as np


def matrix_input():
    choice = True
    while choice:
        zero_sum = 0
        r = int(input('Input number of rows: '))
        c = int(input('Input number of columns: '))
        matrix = np.zeros((r, c))
        for i in range(r):
            for j in range(c):
                print(f'[{i}, {j}]: ', end=' ')
                matrix[i][j] = int(input())
                zero_sum += matrix[i][j]
        print(f'\ninputted matrix: \n\n', matrix := np.matrix(matrix))
        if zero_sum == 0:
            print('you entered correctly zero sum matrix\n')
            break
        else:
            print('your matrix is not zero sum one, press 1 to try\nagain or press enter to use predefined one')
            choice = input('\nyour choice: ')
        return matrix

