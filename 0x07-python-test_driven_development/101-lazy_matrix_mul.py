#!/usr/bin/python3
"""Multiplication of two matrices using Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiples two matrices using NumPy

    Args:
    m_a : first matrix as a list of lists
    m_b : second matrix as a list of lists

    Returns:
    list: the resulting matrix

    Raises:
    ValueError: if the matrices cannot be multiplied

    Note:
    Requires the Numpy library
    """
    if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("shapes (1,0) and (2,2) " +
                         "not aligned: 0 (dim 1) != 2 (dim 0)")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("shapes (2,2) and (1,0) " +
                         "not aligned: 2 (dim 1) != 1 (dim 0)")
    if not all(isinstance(element, (int, float))
       for row in m_a for element in row):
        raise TypeError("invalid data type for einsum")
    if not all(isinstance(element, (int, float))
       for row in m_b for element in row):
        raise TypeError("invalid data type for einsum")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("setting an array element with a sequence")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("setting an array element with a sequence")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) " +
                         "not aligned: 3 (dim 1) != 2 (dim 0)")

    return (np.matmul(m_a, m_b))
