#!/usr/bin/python3
"""
A function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island.
    Args:
        grid (list of list of int): A list of lists where 0 represents
            water and 1 represents land. Each cell is a square with a side
            length of 1. The grid is rectangular, with its width and
            height not exceeding 100.
    Returns:
        int: The perimeter of the island.
    """
    if not isinstance(grid, list) or not all(isinstance(row, list)
                                             for row in grid):
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the cell above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the cell below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the cell to the left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
