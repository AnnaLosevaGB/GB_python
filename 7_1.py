class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        now_str = '\n'
        for i in self.matrix:
            for j in i:
                if now_str[-1] == '\n':
                    now_str = now_str + str(j)
                else:
                    now_str = now_str + '\t' + str(j)
            now_str = now_str + '\n'
        return now_str[1:-1]

    def __add__(self, other):
        new_list_y = []
        while True:
            if len(self.matrix) != len(other.matrix):
                if len(self.matrix) < len(other.matrix):
                    self.matrix.append([0 for i in range(len(self.matrix[0]))])
                else:
                    other.matrix.append([0 for i in range(len(other.matrix[0]))])
            elif len(self.matrix[0]) != len(other.matrix[0]):
                if len(self.matrix[0]) < len(other.matrix[0]):
                    [self.matrix[i].append(0) for i in range(len(self.matrix))]
                else:
                    [other.matrix[i].append(0) for i in range(len(other.matrix))]
            else:
                for i in range(len(self.matrix)):
                    new_list_x = []
                    for j in range(len(self.matrix[i])):
                        new_list_x.append(self.matrix[i][j] + other.matrix[i][j])
                    new_list_y.append(new_list_x)
                return Matrix(new_list_y)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[3, 5], [2, 4], [-1, 64]])
matrix_3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix_4 = Matrix([[1, 1], [1, 1]])
print(matrix_1 + matrix_2 + matrix_3 + matrix_4)
