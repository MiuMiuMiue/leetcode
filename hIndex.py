class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i in range(len(citations)):
            if citations[i] > i:
                h = i + 1
        
        return h

if __name__ == "__main__":
    s = Solution()
    citations = [0]

    print(s.hIndex(citations))
