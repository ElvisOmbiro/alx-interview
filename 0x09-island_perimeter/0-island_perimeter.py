#usr/bin/python3

"""
a function that calculates the perimeter of the island descried i grid above
"""

def island_perimeter(grid):
    """
    args:
        grid: 2D array of 0s and 1s

    Returs:
    Perimeter: the perimeter of the island
    
    """

    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                
                #check right
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

                #check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                #check up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                #check down
                if row == len(grid) -1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter
