class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == 0:
            return 0
        elif dividend == MIN_INT and divisor == -1:
            return MAX_INT
        elif abs(divisor) == 1:
            return dividend if divisor == 1 else dividend * -1

        pos = True
        if (divisor < 0 and dividend > 0) or (dividend < 0 and divisor > 0):
            pos = False

        dividend = dividend if dividend > 0 else dividend * -1
        divisor = divisor if divisor > 0 else divisor * -1

        result = 0
        while dividend >= divisor:
            numberOfDivisor = 1

            tempValue = divisor
            while tempValue + tempValue < dividend:
                tempValue += tempValue
                numberOfDivisor += numberOfDivisor

            dividend -= tempValue
            result += numberOfDivisor

        return result if pos else result * -1

if __name__ == "__main__":
    A = Solution()
    print(A.divide(2, 2))
