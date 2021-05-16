class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = (lambda f: [[matrix[i].__setitem__(j, matrix[i][j] + f(i - 1, j) + f(i, j - 1) - f(i - 1, j - 1)) or matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))])(lambda i, j: matrix[i][j] if i >= 0 and j >= 0 else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (lambda f: f(row2, col2) - f(row1 - 1, col2) - f(row2, col1 - 1) + f(row1 - 1, col1 - 1))(lambda i, j: self.presum[i][j] if i >= 0 and j >= 0 else 0)


# explain
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.presum[i][j]: the range sum from (0,0) to (i,j) in matrix
        self.presum = (
            lambda f:
            [  # add previous values into matrix
                [matrix[i].__setitem__(j, matrix[i][j] + f(i - 1, j) + f(i, j - 1) - f(i - 1, j - 1))
                 or matrix[i][j]  # output matrix
                 for j in range(len(matrix[0]))
                 ]
                for i in range(len(matrix))
            ])(
            lambda i, j: matrix[i][j] if i >= 0 and j >= 0 else 0)  # handle edge cases

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (lambda f:
                f(row2, col2) - f(row1 - 1, col2) - f(row2, col1 - 1) + f(row1 - 1, col1 - 1)
                )(lambda i, j: self.presum[i][j] if i >= 0 and j >= 0 else 0)  # handle edge cases
