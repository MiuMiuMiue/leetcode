class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0

        maxLen = 0
        dpList = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")" and s[i - 1] == "(":
                if i >= 2:
                    dpList[i] = dpList[i - 2] + 2
                    maxLen = max(dpList[i], maxLen)
                else:
                    dpList[i] = 2
                    maxLen = max(dpList[i], maxLen)
            elif s[i] == ")" and s[i - 1] == ")":
                if s[i - dpList[i - 1] - 1] == "(" and i - dpList[i - 1] != 0:
                    dpList[i] = dpList[i - 1] + dpList[i - dpList[i - 1] - 2] + 2
                    maxLen = max(dpList[i], maxLen)

        return maxLen

if __name__ == "__main__":
    A = Solution()
    print(A.longestValidParentheses("(()))())("))
