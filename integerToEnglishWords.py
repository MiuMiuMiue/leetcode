class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        test_list = ["Hundred", "Thousand", "Million", "Billion"]
        oneth = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tenth = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        weird = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        results_list = []

        count = 1
        prev = 0
        temp = ""
        while num > 0:
            digit = num % 10
            if count == 1:
                if digit != 0:
                    temp = oneth[digit - 1]
            elif count == 2:
                if digit == 1 and prev != 0:
                    temp = weird[prev - 1]
                elif digit != 0 and prev != 0:
                    temp = tenth[digit - 1] + ' ' + temp
                elif digit != 0 and prev == 0:
                    temp = tenth[digit - 1]
            elif count == 3:
                if temp == "" and digit != 0:
                    temp = oneth[digit - 1] + ' ' + test_list[0]
                elif digit != 0:
                    temp = oneth[digit - 1] + ' ' + test_list[0] + ' ' + temp
                count = 0
                results_list.append(temp)
                temp = ""
            prev = digit
            count += 1
            num //= 10

        if temp != "":
            results_list.append(temp)


        if len(results_list) == 1:
            return results_list[0]

        result = ""

        for i in range(len(results_list) - 1, -1, -1):
            if i == len(results_list) - 1:
                result = results_list[i] + ' ' + test_list[i]
            elif i > 0:
                if results_list[i] != '':
                    result = result + ' ' + results_list[i] + ' ' + test_list[i]
            else:
                if results_list[i] != '':
                    result = result + ' ' + results_list[i]

        return result

if __name__ == "__main__":
    A = Solution()
    print(A.numberToWords(1000000))
