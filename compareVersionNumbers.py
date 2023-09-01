class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        values1 = []
        values2 = []

        tempVal1 = 0
        for i in range(len(version1) + 1):
            if i == len(version1) or version1[i] == '.':
                values1.append(tempVal1)
                tempVal1 = 0
            elif version1[i] != '.':
                tempVal1 = tempVal1 * 10 + int(version1[i])

        tempVal2 = 0
        for i in range(len(version2) + 1):
            if i == len(version2) or version2[i] == '.':
                values2.append(tempVal2)
                tempVal2 = 0
            elif version2[i] != '.':
                tempVal2 = tempVal2 * 10 + int(version2[i])

        i = 0
        while i < max(len(values1), len(values2)):
            if i >= len(values1):
                if sum(values2[i:]) > 0:
                    return -1
                else:
                    return 0
            elif i >= len(values2):
                if sum(values1[i:]) > 0:
                    return 1
                else:
                    return 0
            elif values1[i] > values2[i]:
                return 1
            elif values2[i] > values1[i]:
                return -1

            i += 1

        return 0


if __name__ == "__main__":
    A = Solution()
    print(A.compareVersion("0.1", "1.1"))