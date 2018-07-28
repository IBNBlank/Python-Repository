# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-04-17 17:50:06
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-28 23:44:08

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


def rowNum(p, sudoku):
    row = set(sudoku[p.y*9:(p.y+1)*9])

    row.remove(0)
    return row


def colNum(p, sudoku):
    col = []
    for i in range(p.x, 81, 9):
        col.append(sudoku[i])

    col = set(col)
    col.remove(0)
    return col


def blockNum(p, sudoku):
    block_x = p.x//3
    block_y = p.y//3
    block = []
    start = block_y*3*9 + block_x*3
    for j in range(3):
        for i in range(start+j*9, start+j*9+3):
            block.append(sudoku[i])

    block = set(block)
    block.remove(0)
    return block


def initPoint(sudoku):
    pointList = []
    for i in range(81):
        if sudoku[i] == 0:
            p = point(i%9, i//9)
            for j in range(1, 10):
                if (j not in rowNum(p, sudoku)) and (j not in colNum(p,sudoku)) and (j not in blockNum(p,sudoku)):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def solveSudoku(sudoku):
    p = pointList.pop()

    for num in p.available:
        p.value = num
        if check(p, sudoku):
            sudoku[p.y*9+p.x] = p.value
            if len(pointList) <= 0:
                print('The right answer is:\n')
                showSudoku(sudoku)
                exit()
            solveSudoku(sudoku)
            sudoku[p.y*9+p.x] = 0
            p.value = 0

    pointList.append(p)


def check(p, sudoku):
    if p.value == 0:
        print('Not assign value to point p!')
        return False
    if (p.value not in rowNum(p, sudoku)) and (p.value not in colNum(p, sudoku)) and (p.value not in blockNum(p, sudoku)):
        return True
    else:
        return False


def showSudoku(sudoku):
    for j in range(9):
        for i in range(9):
            print('{} '.format(sudoku[j*9+i]),end='')
        print('')


if __name__ == '__main__':
    # sudoku = [
    #           8,0,0,0,0,0,0,0,0,
    #           0,0,3,6,0,0,0,0,0,
    #           0,7,0,0,9,0,2,0,0,
    #           0,5,0,0,0,7,0,0,0,
    #           0,0,0,0,4,5,7,0,0,
    #           0,0,0,1,0,0,0,3,0,
    #           0,0,1,0,0,0,0,6,8,
    #           0,0,8,5,0,0,0,1,0,
    #           0,9,0,0,0,0,4,0,0,
    #          ]
    sudoku = [
              0,0,0,2,0,4,0,9,0,
              5,0,0,0,1,0,8,0,4,
              7,3,0,9,0,0,0,0,0,
              0,0,6,0,0,0,0,1,0,
              0,0,9,0,0,0,4,0,0,
              0,5,0,0,0,0,9,0,0,
              0,0,0,0,0,2,0,7,1,
              4,0,5,0,3,0,0,0,2,
              0,1,0,8,0,6,0,0,0,
             ]

    print('The sudoku is:\n')
    showSudoku(sudoku)

    print('\nSolving the problem........\n')
    pointList = initPoint(sudoku)

    solveSudoku(sudoku)

    if len(pointList) > 0:
        print('There is no answer to the sudoku!!!')