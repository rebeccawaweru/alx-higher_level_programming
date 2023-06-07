#!/usr/bin/python3

"""matrix_mul
Multiples two matrices
"""


def matrix_mul(m_a, m_b):
    """ matrix_mul
    Multiplies two matrices.

    Arguments:
    m_a: the first matrix as a list of lists of integers/floats
    m_b: the second matrix as a list of lists of integers/floats

    Returns:
    list: The resulting matrix after multiplication

    Raises:
    TypeError: if m_a or m_b is not a list of lists,
    if one element of the matrices is not an integer/float,
    if m_a or m_b is not a rectangle,
    ValueError: if matrices are empty or cannot be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(element, (int, float))
       for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float))
       for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = [[sum(x * y for x, y in zip(row_x, col_y))
               for col_y in zip(*m_b)] for row_x in m_a]
    return product
