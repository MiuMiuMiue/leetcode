class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            numList = list(self.countAndSay(n - 1))
            result = ""
            prev = numList[0]
            count = 1
            if len(numList) > 1:
                for i in range(1, len(numList)):
                    if numList[i] != prev:
                        result = result + str(count) + prev
                        prev = numList[i]
                        count = 1
                    else:
                        count += 1
                result = result + str(count) + prev
            else:
                result = "11"
            return result





if __name__ == "__main__":
    A = Solution()
    print(A.countAndSay(5))
