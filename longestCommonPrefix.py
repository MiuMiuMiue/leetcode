class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string):
                    return result
                elif string[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result

if __name__ == "__main__":
    A = Solution()
    print(A.longestCommonPrefix(["dog","racecar","car"]))
