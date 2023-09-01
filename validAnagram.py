class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26
        for char in s:
            check[ord(char) - 97] += 1

        for char in t:
            check[ord(char) - 97] -= 1
            if check[ord(char) - 97] < 0:
                return False

        if sum(check) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    s = "rat"
    t = "car"
    S = Solution()
    print(S.isAnagram(s, t))
