class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        start = 0
        curr = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                start = i + 1
        
        if total >= 0:
            return start
        else:
            return -1

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()

    print(s.canCompleteCircuit(gas, cost))
