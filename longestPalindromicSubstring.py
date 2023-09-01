class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        palinList = [['' for x in range(len(s))] for y in range(len(s))]
        index = [0, 0]
        for i in range(len(palinList)):
            for j in range(i + 1):
                if i == j:
                    palinList[i][j] = True
                elif i == j + 1:
                    palinList[i][j] = (s[i] == s[j])
                else:
                    palinList[i][j] = (palinList[i - 1][j + 1] and (s[i] == s[j]))
                if (i - j + 1) > index[1] - index[0] and palinList[i][j]:
                    index = [j, i]
        return s[index[0]:index[1] + 1]

    def longestPalindrome1(self, s: str) -> str:
        if len(s) == 1:
            return s
        maxString = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    testString = s[i:j + 1]
                    if len(testString) > len(maxString):
                        if testString == testString[::-1]:
                            maxString = testString
        return maxString

if __name__ == "__main__":
    A = Solution()
    print(A.longestPalindrome("ANA"))
