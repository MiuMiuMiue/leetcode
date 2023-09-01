class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        j = 0
        while True:
            repeat = 0
            while j < len(chars) and chars[i] == chars[j]:
                repeat += 1
                j += 1
            i += 1
            if repeat > 1 and j < len(chars):
                numOfRepeat = str(repeat)
                for char in numOfRepeat:
                    chars[i] = char
                    i += 1
                for x in range(repeat - 1 - len(numOfRepeat)):
                    chars.pop(i)
                j = i
            elif repeat > 1 and j >= len(chars):
                numOfRepeat = str(repeat)
                for char in numOfRepeat:
                    chars[i] = char
                    i += 1
                for x in range(repeat - 1 - len(numOfRepeat)):
                    chars.pop(i)
                break
            if i >= len(chars):
                break
        return len(chars)

if __name__ == "__main__":
    S = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(S.compress(chars))
    print(chars)
