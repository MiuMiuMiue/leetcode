class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        index = -1
        j = 0
        cont = False

        i = 0
        while i < len(haystack):
            if j >= len(needle):
                return index

            if haystack[i] == needle[j] and cont == False and len(haystack) - i >= len(needle):
                index = i
                j += 1
                cont = True
            elif cont == True and haystack[i] == needle[j]:
                j += 1
            elif cont == True and haystack[i] != needle[j]:
                cont = False
                i = index
                index = -1
                j = 0
            i += 1

        return index

if __name__ == "__main__":
    A = Solution()
    print(A.strStr("mississippi", "pi"))
