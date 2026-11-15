class matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for _ in range(columns)] for _ in range(rows)]

    def assign_values(self, values: list):
        i = 0
        try:
            if len(values) != self.rows * self.columns:
                raise ValueError("The number of values does not match the size of the matrix.")
        except ValueError as e:
            print(e)
            return
        for row in range(self.rows):
            for column in range(self.columns):
                self.matrix[row][column] = values[i]
                i+= 1
    def display(self):
        for row in self.matrix:
            for value in row:
                print(value, end=" ")
            print()

    def get_value(self, row, column):
        return self.matrix[row-1][column-1]

    def set_value(self, row, column, val):
        self.matrix[row-1][column-1] = val

    def add(self, matrix_toadd: matrix):
        try:
            if matrix_toadd.rows != self.rows and matrix_toadd.columns != self.columns:
                raise IndexError("number of rows and columns is not equal")
        except IndexError as e:
            print(e)
            return
        matrix_sum = matrix(self.rows, self.columns)
        for row in self.rows:
            for column in self.columns:
                matrix_sum[row][column] = matrix[row][column] + self.matrix[row][column]
        return matrix