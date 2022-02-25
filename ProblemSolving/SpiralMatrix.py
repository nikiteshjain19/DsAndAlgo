from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = m_len = len(matrix)
        n = n_len = len(matrix[0])
        direction = 1
        i, j = 0, -1
        while len(result) < m_len * n_len:

            for _ in range(n):
                j += direction
                result.append(matrix[i][j])

            m -= 1

            for _ in range(m):
                i += direction
                result.append(matrix[i][j])

            n -= 1

            direction *= -1

        return result


if __name__ == "__main__":
    solution = Solution()
    print("************** Spiral Matrix **************")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.spiralOrder(matrix))
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(solution.spiralOrder(matrix))
