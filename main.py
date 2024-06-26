import numpy as np
from matrix_check import matrix_input


def safe_lines_maxmin(matrix):
    max_in_row = np.max(matrix, axis=0)  # x axis
    min_of_them = np.min(max_in_row)
    safe_position = np.argwhere(max_in_row == min_of_them)
    # print('safe position: ', safe_position)
    amount_safe_lines = safe_position.shape[0]
    # print('amount safe lines: ', amount_safe_lines)
    print('list of safe lines: ')
    for i in range(amount_safe_lines):
        print(safe_position[i][1])
    return min_of_them


def safe_lines_minmax(matrix):
    min_in_col = np.min(matrix, axis=1)  # y axis
    max_of_them = np.max(min_in_col)
    safe_position = np.argwhere(min_in_col == max_of_them)
    amount_safe_lines = safe_position.shape[0]
    # print('amount safe lines: ', amount_safe_lines)
    print('list of safe lines: ')
    for i in range(amount_safe_lines):
        print(safe_position[i][0])
    return max_of_them


if __name__ == '__main__':
    if choice := bool(input('Input "1" to enter data, if not press \nenter to use preset matrix\nyour choice: ')):
        input_matrix = matrix_input()
    else:
        input_matrix = np.matrix([[0, 2, -2, 0, 2, -4],
                                  [-1, -3, 4, 0, 2, 0],
                                  [2, 2, 2, 0, 2, 2],
                                  [-2, 4, -4, 0, 2, 2],
                                  [-2, 4, -4, 0, 2, -2],
                                  [-2, -3, -2, -2, 1, -2]])
        # This is a predefined matrix which you can save for later usages
        print('Sum of predefined matrix in each column is: ', matrix_suma := sum(input_matrix))
        suma_el = 0
        for element in matrix_suma.T:
            suma_el += element
        print('Sum of your matrix: ', suma_el)
        if suma_el != 0:
            print('If you want the game to be fair change values of predefined matrix')
        # this functionality writes down sum of it's elements

    [Ny, Nx] = input_matrix.shape
    role = 'max-min'  # This is a place where you could change your players roles

    print(f'\nMatrix shape is Nx:{Nx}, Ny:{Ny}\n')

    if role == 'max-min':
        input_matrix = np.transpose(input_matrix)
        [Nx, Ny] = input_matrix.shape
        print('The column player minimalize.\n')
        current_strategy = 'min'
    else:  # role == 'min-max'
        print('The row player minimalize')
        current_strategy = 'max'

    if current_strategy == 'max':
        safe_strategy_1 = safe_lines_maxmin(input_matrix)  # y axis
        print('\nSecond player\'s')
        safe_strategy_2 = safe_lines_minmax(input_matrix)
        if safe_strategy_1 == safe_strategy_2:
            print(f'There is the saddle point with a {safe_strategy_1} value')
        else:
            print('There is not a saddle point')

    if current_strategy == 'min':
        safe_strategy_1 = safe_lines_minmax(input_matrix)  # x axis
        print('\nSecond player\'s')
        safe_strategy_2 = safe_lines_maxmin(input_matrix)
        if safe_strategy_1 == safe_strategy_2:
            print(f'There is a saddle point with a {safe_strategy_1} value')
        else:
            print('There is not a saddle point')