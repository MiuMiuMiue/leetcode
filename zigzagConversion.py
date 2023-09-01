class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        multiList = [""] * numRows
        row = 0
        goingDown = True

        index = 0
        while index < len(s):
            if row == numRows - 1:
                goingDown = False
            elif row == 0:
                goingDown = True

            if goingDown == True:
                multiList[row] += s[index]
                row += 1
                index += 1
            elif goingDown == False:
                multiList[row] += s[index]
                row -= 1
                index += 1

        result = "".join(multiList)
        return result

if __name__ == "__main__":
    A = Solution()
    print(A.convert("PAYPALISHIRING", 3))

