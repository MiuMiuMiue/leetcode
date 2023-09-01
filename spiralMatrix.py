class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        i = 0
        j = 0
        total = len(matrix) * len(matrix[0])
        left = False
        right = True
        up = False
        down = False
        while total > 0:
            result.append(matrix[i][j])
            matrix[i][j] = None
            if left:
                if j <= 0 or matrix[i][j - 1] == None:
                    left = False
                    up = True
                    i -= 1
                else:
                    j -= 1
            elif right:
                if j >= len(matrix[0]) - 1 or matrix[i][j + 1] == None:
                    right = False
                    down = True
                    i += 1
                else:
                    j += 1
            elif up:
                if i <= 0 or matrix[i - 1][j] == None:
                    up = False
                    right = True
                    j += 1
                else:
                    i -= 1
            elif down:
                if i >= len(matrix) - 1 or matrix[i + 1][j] == None:
                    down = False
                    left = True
                    j -= 1
                else:
                    i += 1
            total -= 1
        return result

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    S = Solution()
    print(S.spiralOrder(matrix))