# Sudoku-Solver
Here's a 4x4 Sudoku solver written in Python. This version does not utilize the backtracking algorithm, but it covers concepts of list comprehension, matrices, sets, and set theory.

# How does the code work? 
Given a 4x4 sudoku with empty boxes represented by the number 0, the code iterates through the matrix to detect the missing number in the empty squares and returns a fully solved sudoku. When an empty box is found through matrix iteration, all the numbers in the row and column of the designated square are concatenated into an array. Then, the set of the array is taken to remove any duplicate numbers since every row and column of a sudoku contains unique unrepeated values. A 4x4 sudoku only contains numbers from 1-4, so set theory is used to find the number from 1-4 that is not present in the concatenated set of numbers in that row and column. The correct number is inserted into the empty box and the iterator moves to the next empty box. 
