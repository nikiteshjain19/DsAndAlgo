from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_size = len(dungeon)
        col_size = len(dungeon[0])
        dp = [[0 for col in range(col_size)] for row in range(row_size)]

        adj_row_col = [(0, 1), (1, 0)]

        for i in range(row_size - 1, -1, -1):
            for j in range(col_size - 1, -1, -1):
                if i == row_size - 1 and j == col_size - 1:
                    if dungeon[i][j] >= 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dungeon[i][j]
                else:
                    max_ele = float("-inf")
                    for (adj_row, adj_col) in adj_row_col:
                        new_row = i + adj_row
                        new_col = j + adj_col
                        if new_row < row_size and new_col < col_size:
                            max_ele = max(dp[new_row][new_col] + dungeon[i][j], max_ele)
                    if max_ele >= 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = max_ele
        if dp[0][0] >= 0:
            return 1
        else:
            return 0 - dp[0][0] + 1


if __name__ == "__main__":
    solution = Solution()
    matrix = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(solution.calculateMinimumHP(dungeon=matrix))
    matrix = [[-3,5]]
    print(solution.calculateMinimumHP(dungeon=matrix))
    # matrix = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    # print(solution.calculateMinimumHP(dungeon=matrix))
