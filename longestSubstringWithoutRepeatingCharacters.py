class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            testSet = set(s)
            if len(testSet) != len(s):
                len1 = self.lengthOfLongestSubstring(s[1:])
                len2 = self.lengthOfLongestSubstring(s[:len(s) - 1])
                return len1 if len1 > len2 else len2
            elif len(testSet) == len(s):
                return len(s)

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            length1 = 0
            testList = [0] * 128
            for j in range(i, len(s), 1):
                if testList[ord(s[j])] != 0:
                    break
                else:
                    testList[ord(s[j])] = 1
                    length1 += 1
            longest = max(longest, length1)
        return longest

if __name__ == "__main__":
    test = Solution2()
    print(test.lengthOfLongestSubstring("abcabcbb"))

