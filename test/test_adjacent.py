import pytest
from aoch.helpers import adjacent


@pytest.mark.parametrize("position, expeted_result", [
    ([1], [(0,), (2,)]),
    ([5], [(4,), (6,)])
])
def test_adjacent_1d(position, expeted_result):
    assert list(adjacent(position)) == expeted_result

@pytest.mark.parametrize("position, expeted_result", [
    ([0, 0], [(-1, 0), (1, 0), (0, -1), (0, 1)]),
    ((0, 0), [(-1, 0), (1, 0), (0, -1), (0, 1)]),
    ([10, -10], [(9, -10), (11, -10), (10, -11), (10, -9)])
])
def test_adjacent_2d(position, expeted_result):
    assert list(adjacent(position)) == expeted_result

@pytest.mark.parametrize("position, expeted_result", [
    ([0, 0, 0], [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]),
    ((0, 0, 0), [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]),
    ([10, 20, 30], [(9, 20, 30), (11, 20, 30), (10, 19, 30), (10, 21, 30), (10, 20, 29), (10, 20, 31)])
])
def test_adjacent_3d(position, expeted_result):
    assert list(adjacent(position)) == expeted_result