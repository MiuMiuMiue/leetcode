class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        is_row = False
        is_col = False

        for i in range(row):
            for j in range(col):
                if i == 0 and matrix[i][j] == 0:
                    is_row = True
                if j == 0 and matrix[i][j] == 0:
                    is_col = True

                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            if is_col:
                for x in range(row):
                    matrix[x][0] = 0
            
            if is_row:
                for y in range(col):
                    matrix[0][y] = 0

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3,4],
              [5,0,7,8],
              [0,10,11,12],
              [13,14,15,0]]

    s.setZeroes(matrix)
    for row in matrix:
        print(row)
