# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:40:22 2021

@author: seant
"""
import sys 
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

# grid = [
#     [8,0,0,0,0,0,0,0,0],
#     [0,0,3,6,0,0,0,0,0],
#     [0,7,0,0,9,0,2,0,0],
#     [0,5,0,0,0,7,0,0,0],
#     [0,0,0,0,4,5,7,0,0],
#     [0,0,0,1,0,0,0,3,0],
#     [0,0,1,0,0,0,0,6,8],
#     [0,0,8,5,0,0,0,1,0],
#     [0,9,0,0,0,0,4,0,0]]

def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ") 
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") 
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
    if len(empty_positions) == 0:
        print("grid already complete")
        sys.exit()
    return empty_positions

def grid_complete_checker(grid, guesses):
    complete_count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                break
            else:
                complete_count += 1
                if complete_count == len(grid) ** 2:
                    print("Grid Complete!, solution:")
                    print_grid(grid)
                    print("Grid complete in", guesses, "guesses")
                    return True
    return 
    
def row_checker(grid, current_position):
    for i in range(len(grid)):
        element_check = grid[current_position[0]][i] #loop through cols in current row
        if grid[current_position[0]][current_position[1]] == 0:
            row_status = False
        elif element_check == grid[current_position[0]][current_position[1]] and current_position[1] != i and element_check != 0: #checks other elements in row to see if the number is already in row (excluding other empties)
            row_status = False
            break #break out of loop cause not a valid guess
        else: 
            row_status = True
    return row_status

def col_checker(grid, current_position):
    for j in range(len(grid)):
        element_check = grid[j][current_position[1]] #loop through rows in current col
        if grid[current_position[0]][current_position[1]] == 0:
            col_status = False
        elif element_check == grid[current_position[0]][current_position[1]] and current_position[0] != j and element_check != 0: #checks other elements in col to see if the number is already in col (excluding other empties)
            col_status = False
            break #break out of loop cause not a valid guess
        else: 
            col_status = True
    return col_status

def check_local_square(grid, current_position):
   square_row_start = int(current_position[0] / 3) * 3#local square row start index
   square_col_start = int(current_position[1] / 3) * 3 #local square column start index
   for i in range(square_row_start, square_row_start + 3):
       for j in range(square_col_start, square_col_start +3):
           element_check = grid[i][j]
           if grid[current_position[0]][current_position[1]] == 0:
               square_status = False
           elif (element_check == grid[current_position[0]][current_position[1]] and (current_position[0] != i or current_position[1] != j) and element_check != 0): #checks other elements in local square to see if the number is already in row (excluding other empties)
               square_status = False
               return square_status #could use breaks (2, 1 per loop) and contiunue
           else: 
               square_status = True
   return square_status

if __name__ == "__main__":
    empty_spaces = find_empty_spaces(grid)
    empty_space_index = 0 #start with first empty element
    guess_start = 1
    guesses = 0
    while True: #indefinite loop
        current_position = empty_spaces[empty_space_index]
        for guess in range(guess_start, 10): #take current position and try numbers 1 to 9, perform tests to see if all pass
            guesses += guesses
            grid[current_position[0]][current_position[1]] = guess
            if guess_start == 9:
                empty_space_index = empty_space_index - 1
                grid[current_position[0]][current_position[1]] = 0
                if grid[empty_spaces[empty_space_index][0]][empty_spaces[empty_space_index][1]] == 9:
                    guess_start = 9
                    break
                else:
                    guess_start = grid[empty_spaces[empty_space_index][0]][empty_spaces[empty_space_index][1]] + 1
                    break
                break
            if row_checker(grid, current_position) == True and col_checker(grid, current_position) == True and check_local_square(grid, current_position) == True:
                if grid_complete_checker(grid, guesses) == True:   
                    sys.exit()
                else:
                    empty_space_index = empty_space_index + 1
                    guess_start = 1
                break          
            elif guess == 9:
                empty_space_index = empty_space_index - 1
                grid[current_position[0]][current_position[1]] = 0
                if grid[empty_spaces[empty_space_index][0]][empty_spaces[empty_space_index][1]] == 9:
                    guess_start = 9
                    break
                else:
                    guess_start = grid[empty_spaces[empty_space_index][0]][empty_spaces[empty_space_index][1]] + 1
                    break
            else:
                continue

        
        

    
    
    






















