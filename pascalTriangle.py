class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for rowNum in range(1, numRows + 1):
            row = []
            for i in range(rowNum):
                if i == 0 or i == rowNum - 1:
                    row.append(1)
                else:
                    row.append(result[rowNum - 2][i - 1] + result[rowNum - 2][i])
            result.append(row)
        return result

if __name__ == "__main__":
    S = Solution()
    print(S.generate(5))