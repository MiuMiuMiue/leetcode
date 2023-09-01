import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chrDict = collections.defaultdict(int)
        for char in s:
            chrDict[char] += 1

        for char in chrDict:
            if chrDict[char] == 1:
                return s.index(char)
        return -1