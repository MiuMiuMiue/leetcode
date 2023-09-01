class Solution:
    digitDict = {2: "abc",
                 3: "def",
                 4: "ghi",
                 5: "jkl",
                 6: "mno",
                 7: "pqrs",
                 8: "tuv",
                 9: "wxyz"}

    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        allCombinations = []
        def getAll(index, current):
            if len(current) == len(digits):
                allCombinations.append(current)
                return

            for char in self.digitDict[int(digits[index])]:
                current += char
                getAll(index + 1, current)
                current = current[0:len(current) - 1]

        getAll(0, "")
        return allCombinations

if __name__ == "__main__":
    A = Solution()
    print(A.letterCombinations("23"))