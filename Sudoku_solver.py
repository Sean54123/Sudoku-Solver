# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:40:22 2021

@author: seant
"""
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ") #starts new line afterwards
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") #ends with no space rather than starting a new line (default for print statement)
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end = "")
                
def find_empty_spaces(grid):
    empty_positions = []
    for i in range(len(grid)):
       for j in range(len(grid)):
            if grid[i][j] == 0:
                empty_positions.append([i, j])
    print(len(empty_positions))
    return empty_positions

def grid_complete_checker(grid):
    complete_count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                break
            else:
                complete_count =+ 1
                if complete_count == len(grid) ** 2:
                    print("Grid Complete!, solution:")
                    print_grid(grid)
    print("Not Complete")
    
def row_checker(grid, current_position):
    for i in range(len(grid)):
        element_check = grid[current_position[0]][i]
        if grid[current_position[0]][current_position[1]] == 0:
            print("Please enter guess in element")
        elif element_check == grid[current_position[0]][current_position[1]] and element_check != 0: #checks other elements in rows to see if the number is already in row
            break #break out of loop cause not a valid guess
    
    return row_status



                    
#functions needed: row checker, column checker, local square checker, back tracker, main code flow
            
print_grid(grid)
empty_spaces = find_empty_spaces(grid) #have one as initial empty space at start of main flow
current_position = empty_spaces[0]
grid_complete_checker(grid)

