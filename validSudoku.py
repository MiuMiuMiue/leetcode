class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        checkRow = [[] for i in range(9)]
        checkCol = [[] for i in range(9)]
        checkBox = [[] for i in range(9)]
        for row in range(9):
            for col in range(9):
                temp = board[row][col]

                if temp == ".":
                    continue

                if temp in checkRow[row]:
                    return False
                checkRow[row].append(temp)

                if temp in checkCol[col]:
                    return False
                checkCol[col].append(temp)

                index = (row // 3) * 3 + col // 3
                if temp in checkBox[index]:
                    return False
                checkBox[index].append(temp)
        return True

if __name__ == "__main__":
    tempList = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    A = Solution()
    print(A.isValidSudoku(tempList))
