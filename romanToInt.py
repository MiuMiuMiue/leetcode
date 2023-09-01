class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        result = 0
        last = True

        i = 0
        while i < len(s) - 1:
            if romanDict[s[i]] < romanDict[s[i + 1]]:
                result += (romanDict[s[i + 1]] - romanDict[s[i]])
                if i == len(s) - 2:
                    last = False
                i += 1
            else:
                result += romanDict[s[i]]
            i += 1

        if last == True:
            result += romanDict[s[-1]]

        return result

if __name__ == "__main__":
    A = Solution()
    print(A.romanToInt("MCMXCIV"))
