#!/usr/bin/python3
"""Module that multiply tow matrix
"""


def matrix_mul(m_a, m_b):
    """  function that multiplies 2 matrices  """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(ro, list) for ro in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ro, list) for ro in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for i in m_a for num in i]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for i in m_b for num in i]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(item) == len(m_a[0]) for item in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(item) == len(m_b[0]) for item in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inv_B1 = []
    for item in range(len(m_b[0])):
        tmp = []
        for nm in range(len(m_b)):
            tmp.append(m_b[nm][item])
        inv_B1.append(tmp)
    result = []
    for item in m_a:
        tmp_1 = []
        for col in inv_B1:
            mul = 0
            for i in range(len(inv_B1[0])):
                mul += item[i] * col[i]
            tmp_1.append(mul)
        result.append(tmp_1)
    return result
