class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        one = 1
        index = len(digits) - 1

        while one == 1 and index >= 0:
            digits[index] += 1
            if digits[index] < 10:
                one = 0
            else:
                digits[index] = 0
                index -= 1

        if index == -1 and one == 1:
            digits[0] += 1
            digits.append(0)

        return digits

if __name__ == "__main__":
    A = Solution()
    num = [9]
    print(A.plusOne(num))