class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def addParenthesis(temp, left=0, right=0):
            if len(temp) == 2 * n:
                result.append(temp)
                return

            if left == right:
                addParenthesis(temp + "(", left + 1, right)
            elif right < left and left == n:
                addParenthesis(temp + ")", left, right + 1)
            else:
                addParenthesis(temp + "(", left + 1, right)
                addParenthesis(temp + ")", left, right + 1)

        addParenthesis("")
        return result

if __name__ == "__main__":
    A = Solution()
    print(A.generateParenthesis(8))