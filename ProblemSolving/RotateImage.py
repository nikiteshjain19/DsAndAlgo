from typing import List


class Solution:
    def transpose_reflect(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

        return matrix

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix


if __name__ == "__main__":
    solution = Solution()
    print("************** Transpose and reflect **************")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.transpose_reflect(matrix))
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(solution.transpose_reflect(matrix))

    print("************** Rotate **************")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.rotate(matrix))
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(solution.rotate(matrix))
