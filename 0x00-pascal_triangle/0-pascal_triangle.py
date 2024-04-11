def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.
    Args:
    - n (int): The number of rows in the Pascal's triangle.
    Returns:
    -list of lists of integers: Pascal's triangle represented as list of list
   """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
