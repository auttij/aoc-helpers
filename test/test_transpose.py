import pytest
from aoch.helpers import transpose

def test_basic():
    matrix = [[1, 2], [3, 4]]
    t = transpose(matrix)
    dt = transpose(t)
    assert t == [[1, 3], [2, 4]]
    assert dt == matrix

def test_non_square():
    matrix = [[1, 2, 3, 4]]
    t = transpose(matrix)
    dt = transpose(t)
    assert t == [[1], [2], [3], [4]]
    assert dt == matrix
