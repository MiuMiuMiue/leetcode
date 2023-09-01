class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        oneth = ['I', "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tenth = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundred = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thouthand = ["M", "MM", "MMM"]
        romans = [oneth, tenth, hundred, thouthand]
        count = 1000
        j = 3

        while num != 0:
            i = num // count
            num %= count
            count //= 10
            if i != 0:
                result += romans[j][i - 1]
            j -= 1

        return result