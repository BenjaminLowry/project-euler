import math
from pathlib import Path


def solution() -> int:
    matrix = read_matrix()
    sum_matrix = []

    for i in range(len(matrix)):
        row = matrix[i]
        sum_row = []
        for j in range(len(row)):
            if i == 0 and j == 0:
                sum_row.append(row[j])
                continue

            prev_i_sum = sum_matrix[i - 1][j] if i - 1 >= 0 else math.inf
            prev_j_sum = sum_row[j - 1] if j - 1 >= 0 else math.inf
            sum_row.append(min(prev_i_sum, prev_j_sum) + row[j])
        sum_matrix.append(sum_row)
    return sum_matrix[-1][-1]


def read_matrix() -> list[list[int]]:
    filename = "../resources/0081_matrix.txt"
    text = Path(filename).read_text()
    res = []
    for line in text.splitlines():
        res.append([int(x) for x in line.split(",")])
    return res
