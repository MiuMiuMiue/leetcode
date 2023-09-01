class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False

        newNum = 0
        newX = x

        while newX > 0:
            temp = newX % 10
            newNum = newNum * 10 + temp
            newX //= 10

        if newNum == x:
            return True
        return False

if __name__ == "__main__":
    A = Solution()
    print(A.isPalindrome(121))
