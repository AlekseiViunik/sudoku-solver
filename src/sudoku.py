
from copy import deepcopy
from time import process_time
from os.path import join, abspath 


TASK_PATH = join('.', 'Data', 'sudoku3.txt')
TASK_PATH = abspath(TASK_PATH)

BLOCK_DIMENSION = 3
SUDO_DIMENSION = 9


def solve(sudo):
    '''Calls solution function (solve_step) for current sudoku. 
    Returns solved sudoku.'''
    sol = [[y for y in x] for x in sudo]
    if solve_step(sol):
        return sol

def solve_step(solution):
    '''Runs through the sudoku and fills cells which have only one
    solution. If it doesn't any one-solution cell, it calls a recursion 
    for the min_pos cell. Returns solved sudoku or None.'''
    while True:
        min_pos = None        # A cell which have min amount of possible values 
        for row_index in range(SUDO_DIMENSION):
            for column_index in range(SUDO_DIMENSION):
                if solution[row_index][column_index]:
                    continue
                pos_value = get_possible_value(
                    row_index, column_index, solution
                )
                pos_value_count = len(pos_value)
                if not pos_value_count:
                    return False
                if pos_value_count == 1:
                    solution[row_index][column_index], = pos_value
                if not min_pos or pos_value_count < len(min_pos[1]):
                    min_pos = (row_index, column_index), pos_value
        if not min_pos:
            return True
        elif len(min_pos[1]) >=2:
            break
    (row, column), values = min_pos
    for value in values:
        solution_copy = deepcopy(solution)
        solution_copy[row][column] = value
        if solve_step(solution_copy):
            for row in range(SUDO_DIMENSION):
                for column in range(SUDO_DIMENSION):
                    solution[row][column] = solution_copy[row][column]
            return True




def get_row_value(row_index, sudo):
    '''For each row returns which numbers it has.'''
    return set(sudo[row_index])

def get_column_value(column_index, sudo):
    '''For each column returns which numbers it has.'''
    return {line[column_index] for line in sudo} # generator expression

def get_block_value(row_index, column_index, sudo):
    '''For each block 3x3 returns which numbers it has.'''
    block_row_start = 3 * (row_index // 3)
    block_column_start = 3 * (column_index // 3)
    return {
        sudo[block_row_start + x][block_column_start + y]
        for x in range(BLOCK_DIMENSION)
        for y in range(BLOCK_DIMENSION)
    }

def get_possible_value(row_index, column_index, sudo):
    '''For current cell returns possible values.'''
    result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    result -= get_row_value(row_index, sudo)
    result -= get_column_value(column_index, sudo)
    result -= get_block_value(row_index, column_index, sudo)
    return result

def print_sudoku(s):
    '''Makes the output sudoku readable.'''
    print('+-------+-------+-------+')
    for k in range(SUDO_DIMENSION):
        print('|', s[k][0], s[k][1], s[k][2], '|',
                   s[k][3], s[k][4], s[k][5], '|',
                   s[k][6], s[k][7], s[k][8], '|',)
        if k % 3 == 2:
            print('+-------+-------+-------+')

def sudoku_conversion(string_sudoku):
    ''' Get string as an argument. It contains 81 numbers from 0 to 9. 
    Returns list of 9 lists with 9 numbers inside.'''
    sodoku = [
        [*map(
            int, string_sudoku[i:i+SUDO_DIMENSION]
        )] for i in range(0, SUDO_DIMENSION**2, SUDO_DIMENSION)
    ]
    return sodoku

sudo = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],

    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],

    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

with open(TASK_PATH, 'rt', encoding='UTF-8') as source:
    for line in source:
        line = line.strip()
        if len(line) == 81:
            print(line)
            sudo_list = sudoku_conversion(line)
            print_sudoku(sudo_list)





#print_sudoku(sudo)
#time_start = process_time()
#result = solve(sudo)
#time_solve = process_time() - time_start
#if result:
#    solve_step(sudo)
#    print_sudoku(result)
#    print(f'Sudoku has solved for {time_solve} sec.')
#else:
#    print(f'Sudoku has not solved for {time_solve} sec.')
#print('END')