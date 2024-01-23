def transpose(matrix: list[list[int]]) -> list[list[int]]:
	'''transposes a matrix'''
	rows = len(matrix)
	column = len(matrix[0])
	result = [[0 for i in range(rows)] for j in range(column)]

	for r in range(rows):
		for c in range(column):
			result[c][r] = matrix[r][c]
	return result

def adjacent(pos):
    for axis in range(len(pos)):
        for d in (-1, 1):
            q = list(pos)
            q[axis] += d
            yield tuple(q)
