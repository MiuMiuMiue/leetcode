class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        intString = str(x)[1:] if neg == True else str(x)
        intString = intString[::-1]
        if (neg == True and int(intString) > 2 ** 31) or (neg == False and int(intString) > 2 ** 31 - 1):
            return 0
        result = -int(intString) if neg == True else int(intString)
        return result

    def reverse1(self, x: int) -> int:
        neg = True if x < 0 else False
        x = -x if neg == True else x
        result = 0
        while x != 0:
            temp = x % 10
            x //= 10
            result *= 10
            result += temp
            if result < -1 * (2 ** 31) or result > 2 ** 31 - 1:
                return 0
        result = -result if neg == True else result
        return result

if __name__ == "__main__":
    x = -32
    T = Solution()
    print(T.reverse1(x))
