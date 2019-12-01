class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        num_cells = 0
        for r in range(n):
            matrix.append([0 for c in range(m)])

        for i in indices:
            ri = i[0]
            ci = i[1]
            for j in range(len(matrix[ri])):
                matrix[ri][j] += 1
            for j in range(len(matrix)):
                matrix[j][ci] += 1

        for row in matrix:
            for element in row:
                if element % 2:
                    num_cells += 1
        return num_cells
