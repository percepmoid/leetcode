class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        length = len(grid)
        difference = 0
        left = []
        top = [[0 for i in range(length)]]

        for i in range(length):
            left.append(max(grid[i]))
        for j in range(length):
            for i in range(length):
                top[0][i] = grid[i][j]
            top.append(max(top[0]))
        del(top[0])


        for i in range(length):
            for j in range(length):
                difference += min(left[i], top[j]) - grid[i][j]

        return difference
