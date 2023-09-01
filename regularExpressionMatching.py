class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = None
        cont = False

        for chr in s:
            if p == "":
                return False
            if p[0] == '*':
                cont = True
                p = p[1:]
                result = True
            elif p[0] == '.':
                p = p[1:]
                cont = False
            elif chr == p[0]:
                cont = False
                p = p[1:]
            elif cont == False and chr != p[0]:
                p = p[1:]
                result = False

        return result

if __name__ == "__main__":
    # A = Solution()
    # print(A.isMatch("mississippi", "mis*is*p*."))
    from pathlib import Path
    a = Path.cwd()
    for file in a.iterdir():
        print(file)

