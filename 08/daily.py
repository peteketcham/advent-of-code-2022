"""
    '(shrugs)'
    --Ada
"""


from pprint import pprint
import numpy as np


def main():
    """pass"""
    # test = ["30373", "25512", "65332", "33549", "35390"]
    matrix = []
    with open("input.txt", "r", encoding="UTF-8") as file:
        file = [x.strip("\n") for x in file]
        # file = test
        for line in file:
            matrix.append([int(x) for x in list(line)])
        # matrix_rotate = list(zip(*matrix[::-1]))
    # identity matrixes for counting totals
    id_matrix = np.ones((len(matrix[0]), len(matrix)), dtype=int)
    # id_sum = np.sum(id_matrix)
    for row_index, row in enumerate(matrix):
        for index, value in enumerate(row):
            column = [x[index] for x in matrix]
            # eliminate edges
            if (
                index == 0
                or index == len(row) - 1
                or row_index == 0
                or row_index == len(matrix) - 1
            ):
                id_matrix[row_index][index] = 0
                continue

            # check row
            # left
            if row[:index]:
                # # pt1
                # if max(row[:index]) < value:
                #     id_matrix[row_index][index] = 0
                # pt2
                try:
                    left_multiplier = 1 + next(
                        x for x, val in enumerate(reversed(row[:index])) if val >= value
                    )
                except StopIteration as _:
                    left_multiplier = len(row[:index])
            # right
            if row[index + 1 :]:
                # # pt1
                # if max(row[index + 1 :]) < value:
                #     id_matrix[row_index][index] = 0
                # pt2
                try:
                    right_multiplier = 1 + next(
                        x for x, val in enumerate(row[index + 1 :]) if val >= value
                    )
                except StopIteration as _:
                    right_multiplier = len(row[index + 1 :])

            # check column
            # above
            if column[:row_index]:
                # # pt1
                # if max(column[:row_index]) < value:
                #     id_matrix[row_index][index] = 0
                # pt2
                try:
                    up_multiplier = 1 + next(
                        x
                        for x, val in enumerate(reversed(column[:row_index]))
                        if val >= value
                    )
                except StopIteration as _:
                    up_multiplier = len(column[:row_index])
            # below
            if column[row_index + 1 :]:
                # # pt1
                # if max(column[row_index + 1 :]) < value:
                #     id_matrix[row_index][index] = 0
                # pt2
                try:
                    down_multiplier = 1 + next(
                        x
                        for x, val in enumerate(column[row_index + 1 :])
                        if val >= value
                    )
                except StopIteration as _:
                    down_multiplier = len(column[row_index + 1 :])
            id_matrix[row_index][index] = (
                up_multiplier * down_multiplier * left_multiplier * right_multiplier
            )
    pprint(id_matrix)
    print(np.max(id_matrix))
    # print(sum(sum(x) for x in id_matrix), id_sum, id_sum - sum(sum(x) for x in id_matrix))


if __name__ == "__main__":
    main()
