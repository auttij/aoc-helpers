def transpose(matrix: list[list[int]]) -> list[list[int]]:
	'''transposes a matrix'''
	rows = len(matrix)
	column = len(matrix[0])
	result = [[0 for i in range(rows)] for j in range(column)]

	for r in range(rows):
		for c in range(column):
			result[c][r] = matrix[r][c]
	return result

def binarySearch(arr, target):
	lo, hi = 0, len(arr) - 1
	while lo <= hi:
		m = (lo + hi) // 2
		if arr[m] < target:
			lo = m + 1
		elif arr[m] > target:
			hi = m - 1
		else:
			return m
	return -1

def adjacent(pos):
    for axis in range(len(pos)):
        for d in (-1, 1):
            q = list(pos)
            q[axis] += d
            yield tuple(q)

def neighbors(pos):
	from itertools import product
	dimensions = len(pos)
	combinations = product([-1, 0, 1], repeat=dimensions)
	for it in combinations:
		if not any(it):
			continue
		yield tuple(sum(i) for i in zip(it, pos))
