class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        if s == "":
            return 0
        neg = True if s[0] == "-" else False
        s = s[1:] if neg == True or s[0] == "+" else s
        s += " "
        result = 0

        while 48 <= ord(s[0]) <= 57:
            temp = s[0]
            tempResult = result * 10 + int(temp)
            if (neg == True and tempResult > 2 ** 31) or (neg == False and tempResult > 2 ** 31 - 1):
                maxVal = -1 * 2 ** 31 if neg == True else 2 ** 31 - 1
                return maxVal
            result = tempResult
            s = s[1:]

        result = -result if neg == True else result
        return result

if __name__ == "__main__":
    A = Solution()
    print(A.myAtoi("   32231321 fdsfsd"))
