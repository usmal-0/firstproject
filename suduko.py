from  sudoku import Sudoku
from sudoku_sol import *

puzzle = Sudoku().difficulty(0.9)
puzzle.show()

solution = puzzle.solve()
solution.show()