"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        #1 version: 36ms
        """
        # if not board:
        #     return None
        # if not board[0]:
        #     return None
        # assert(0 < len(board) )
        # assert(0 < len(board[0]))
        # m, n = len(board), len(board[0])
        # c = [ [0]*(n+2) for _ in range(m+2) ]
        # live = 3
        # die = [0,1,4,5,6,7,8]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         c[i][j] = board[i-1][j-1]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         count = sum([c[i+x][j+y] for x in range(-1,2) for y in range(-1,2) if not (x==y==0)])
        #         if count == live:
        #             board[i-1][j-1] = 1
        #         elif count in die:
        #             board[i-1][j-1] = 0
        #         elif count == 2:
        #             continue
        #         else: # out of range
        #             raise ValueError('value out of range [0, 8].')
        """
        #2 version
        """
        if not board:
            return None
        if not board[0]:
            return None
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] += 2 * sum([board[i+x][j+y]%2 for x in range(-1,2) for y in range(-1,2) if ((0 <= i+x < m) and (0 <=j+y < n) and not (x == 0 and y == 0))])
                
        die = set([0,1,4,5,6,7,8])
        for i in range(m):
            for j in range(n):
                count = board[i][j] // 2
                if count == 3:
                    board[i][j] = 1
                elif count in die:
                    board[i][j] = 0
                else:
                    board[i][j] %= 2