class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num11 = 0
        num22 = 0
        while num1:
            temp = num1[0]
            num11 *= 10
            num11 += ord(temp) - 48
            num1 = num1[1:]

        while num2:
            temp = num2[0]
            num22 *= 10
            num22 += ord(temp) - 48
            num2 = num2[1:]

        return str(num11 * num22)

print(ord("1"))
print(ord('2'))